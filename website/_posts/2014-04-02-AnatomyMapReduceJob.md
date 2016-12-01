---
layout: post
title: Anatomy of a MapReduce Job
---

In MapReduce, a YARN application is called a **Job**. The implementation of the Application Master provided by the MapReduce framework is called **`MRAppMaster`**.

### <a href="#timeline-of-a-mapreduce-job" id="timeline-of-a-mapreduce-job">Timeline of a MapReduce Job</a>
![Timeline MapReduce Job](public/images/timeline-mapreduce-job_534c0041-2498-44cd-9480-18910a008c0f.png)
This is the timeline of a MapReduce Job execution:

 * **Map Phase**: several **Map Tasks** are executed
 * **Reduce Phase**: several **Reduce Tasks** are executed

Notice that the Reduce Phase may start before the end of Map Phase. Hence, an interleaving between them is possible.

### <a href="#map-phase" id="map-phase">Map Phase</a>
We now focus our discussion on the Map Phase. A key decision is how many MapTasks the Application Master needs to start for the current job.

#### <a href="#what-does-the-user-give-us" id="what-does-the-user-give-us">What does the user give us?</a>
Let's take a step back. When a client submits an application, several kinds of information are provided to the YARN infrastucture. In particular:

 * a configuration: this may be partial (some parameters are not specified by the user) and in this case the default values are used for the job. Notice that these default values may be the ones chosen by a Hadoop provider like Amanzon.
 * a JAR containing:
   * a `map()` implementation
   * a combiner implementation
   * a `reduce()` implementation
 * input and output information:
   * input directory: is the input directory on HDFS? On S3? **How many files?**
   * output directory: where will we store the output? On HDFS? On S3?

The number of files inside the input directory is used for deciding the number of Map Tasks of a job.

#### <a href="#how-many-map-tasks" id="how-many-map-tasks">How many Map Tasks?</a>
The Application Master will launch one MapTask for each map split. Typically, there is a map split for each input file. If the input file is too big (bigger than the HDFS block size) then we have two or more map splits associated to the same input file. This is the pseudocode used inside the method `getSplits()` of the `FileInputFormat` class:

    num_splits = 0
    for each input file f:
       remaining = f.length
       while remaining / split_size > split_slope:
          num_splits += 1
          remaining -= split_size
where:

    split_slope = 1.1
    split_size =~ dfs.blocksize

Notice that the configuration parameter `mapreduce.job.maps` is ignored in MRv2 (in the past it was just an hint).

#### <a href="#maptask-launch" id="maptask-launch">MapTask Launch</a>

The MapReduce Application Master asks to the Resource Manager for Containers needed by the Job: one MapTask container request for each MapTask (map split).

A container request for a MapTask tries to exploit data locality of the map split. The Application Master asks for:

 * a container located on the same Node Manager where the map split is stored (a map split may be stored on multiple nodes due to the HDFS replication factor);
 * otherwise, a container located on a Node Manager in the same rack where the the map split is stored;
 * otherwise, a container on any other Node Manager of the cluster

This is just an hint to the Resource Scheduler. The Resource Scheduler is free to ignore data locality if the suggested assignment is in conflict with the Resouce Scheduler's goal.

When a Container is assigned to the Application Master, the MapTask is launched.

#### <a href="#map-phase-example-of-an-execution-scenario" id="map-phase-example-of-an-execution-scenario">Map Phase: example of an execution scenario</a>
![Map Phase execution](public/images/map-phase-execution_536a0a11-2ac8-4721-9bfb-3c730a004de9.png)

This is a possible execution scenario of the Map Phase:

 * there are two Node Managers: each Node Manager has 2GB of RAM (NM capacity) and each MapTask requires 1GB, we can run in parallel 2 containers on each Node Manager (this is the best scenario, the Resource Scheduler may decide differently)
 * there are no other YARN applications running in the cluster
 * our job has 8 map splits (e.g., there are 7 files inside the input directory, but only one of them is bigger than the HDFS block size so we split it into 2 map splits): we need to run 8 Map Tasks.

#### <a href="#map-task-execution-timeline" id="map-task-execution-timeline">Map Task Execution Timeline</a>
![Map Task Execution Timeline](public/images/map-task-execution-timeline_534c1cfb-be48-4146-bbe3-040a0a005d90.png)
Let's now focus on a single Map Task. This is the Map Task execution timeline:

 * **INIT** phase: we setup the Map Task
 * **EXECUTION** phase: for each (key, value) tuple inside the map split we run the `map()` function
 * **SPILLING** phase: the map output is stored in an in-memory buffer; when this buffer is *almost* full then we start (in parallel) the spilling phase in order to remove data from it
 * **SHUFFLE** phase: at the end of the spilling phase, we merge all the map outputs and package them for the reduce phase

#### <a href="#maptask-init" id="maptask-init">MapTask: INIT</a>

During the INIT phase, we:

 1. create a context (`TaskAttemptContext.class`)
 2. create an instance of the user `Mapper.class`
 3. setup the input (e.g., `InputFormat.class`, `InputSplit.class`, `RecordReader.class`)
 4. setup the output (`NewOutputCollector.class`)
 5. create a mapper context (`MapContext.class`, `Mapper.Context.class`)
 6. initialize the input, e.g.:
   * create a `SplitLineReader.class` object
   * create a `HdfsDataInputStream.class` object

#### <a href="#maptask-execution" id="maptask-execution">MapTask: EXECUTION</a>

![MapTask execution](public/images/maptask-execution_534fb31a-ae3c-4373-ae87-30b60a00c52e.png)

The EXECUTION phase is performed by the `run` method of the `Mapper` class. The user can override it, but by default it will start by calling the `setup` method: this function by default does  not do anything useful but can be override by the user in order to setup the Task (e.g., initialize class variables).
After the setup, for each <key, value> tuple contained in the map split, the `map()` is invoked. Therefore, `map()` receives: a key a value, and a mapper context. Using the context, a `map` stores its  output to a buffer.

Notice that the map split is fetched chuck by chunk (e.g., 64KB) and each chunk is split in several (key, value) tuples (e.g., using `SplitLineReader.class`). This is done inside the `Mapper.Context.nextKeyValue` method.

When the map split has been completely processed, the `run` function calls the `clean` method: by default, no action is performed but the user may decide to override it.

#### <a href="#maptask-spilling" id="maptask-spilling">MapTask: SPILLING</a>

![Spilling phase](public/images/spilling-phase_534fcae9-b818-4e6f-bb3e-380f0a00c52e.png)

As seen in the EXECUTING phase, the `map` will write (using `Mapper.Context.write()`) its output into a circular in-memory buffer (`MapTask.MapOutputBuffer`). The size of this buffer is fixed and determined by the configuration parameter `mapreduce.task.io.sort.mb` (default: 100MB).

Whenever this circular buffer is *almost* full (`mapreduce.map.
sort.spill.percent`: 80% by default), the SPILLING phase is performed (in parallel using a separate thread). Notice that if the splilling thread is too slow and the buffer is 100% full, then the `map()` cannot be executed and thus it has to wait.

The SPILLING thread performs the following actions:

 1. it creates a `SpillRecord` and `FSOutputStream` (local filesystem)
 2. in-memory sorts the used chunk of the buffer: the output tuples are sorted by (partitionIdx, key) using a quicksort algorithm.
 3. the sorted output is split into partitions: one partition for each ReduceTask of the job (see later).
 4. Partitions are sequentially written into the local file.

##### <a href="#how-many-reduce-tasks" id="how-many-reduce-tasks">How Many Reduce Tasks?</a>

The number of ReduceTasks for the job is decided by the configuration parameter `mapreduce.job.reduces`.

#### <a href="#what-is-the-partitionidx-associated-to-an-output-tuple" id="what-is-the-partitionidx-associated-to-an-output-tuple">What is the partitionIdx associated to an output tuple?</a>

The paritionIdx of an output tuple is the index of a partition. It is decided inside the `Mapper.Context.write()`:

    partitionIdx = (key.hashCode() & Integer.MAX_VALUE) % numReducers

It is stored as metadata in the circular buffer alongside the output tuple. The user can customize the partitioner by setting the configuration parameter `mapreduce.job.partitioner.class`.

#### <a href="#when-do-we-apply-the-combiner" id="when-do-we-apply-the-combiner">When do we apply the combiner?</a>

If the user specifies a combiner then the SPILLING thread, before writing the tuples to the file (4), executes the combiner on the tuples contained in each partition. Basically, we:

 1. create an instance of the user `Reducer.class` (the one specified for the combiner!)
 2. create a `Reducer.Context`: the output will be stored on the local filesystem
 3. execute `Reduce.run()`: see Reduce Task description

The combiner typically use the same implementation of the
standard `reduce()` function and thus can be seen as a local reducer.

### <a href="#maptask-end-of-execution" id="maptask-end-of-execution">MapTask: end of EXECUTION</a>

At the end of the EXECUTION phase, the SPILLING thread is triggered for the last time. In more detail, we:

 1. sort and spill the remaining unspilled tuples
 2. start the SHUFFLE phase

Notice that for each time the buffer was almost full, we get one spill file (`SpillReciord` + output file). Each Spill file contains several partitions (segments).

#### <a href="#maptask-shuffle" id="maptask-shuffle">MapTask: SHUFFLE</a>

### <a href="#reduce-phase" id="reduce-phase">Reduce Phase</a>

[...]

### <a href="#yarn-and-mapreduce-interaction" id="yarn-and-mapreduce-interaction">YARN and MapReduce interaction</a>
![YARN and MapReduce interaction](public/images/yarn-and-mapreduce-interaction_53302af2-7d38-412b-8275-6ffe0a009433.png)

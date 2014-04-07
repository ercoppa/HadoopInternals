---
layout: post
title: Hadoop Configuration parameters
---
Parameter | File | Default | Diagram(s)
------------- | -------------  | ------------- | ------------- 
`mapreduce.task.io.sort.mb`  | `mapred-site.xml` | 100 | [MapTask > Shuffle](MapTask.html#post-execution-shuffle) 
 | | | [MapTask > Execution](MapTask.html#execution)
`mapreduce.map.sort.spill.percent`  | `mapred-site.xml` | 0.80 | [MapTask > Shuffle](MapTask.html#post-execution-shuffle) 
 | | | [MapTask > Execution](MapTask.html#execution)
`mapreduce.task.io.sort.factor`   | `mapred-site.xml` | 100 | [MapTask > Shuffle](MapTask.html#post-execution-shuffle) 
 | | | [Merge](MapReduceMerge.html)
 | | | [ReduceTask > Shuffle](ReduceTask.html#shuffle-merge)
`mapreduce.map.combine.minspills`  | `mapred-site.xml` | 3 | [MapTask > Shuffle](MapTask.html#post-execution-shuffle) 
`mapreduce.job.reduces`  | `mapred-site.xml` | 1 | [MapTask > Shuffle](MapTask.html#post-execution-shuffle) 
 | | 0 | [Job > NEW => INITED](Job.html#new-inited-job-init) 
`mapreduce.cluster.local.dir`  | `mapred-site.xml` | `${hadoop.tmp.dir}`/mapred/local | [MapTask > Shuffle](MapTask.html#post-execution-shuffle) 
`mapreduce.reduce.merge.memtomem.enabled` | `mapred-site.xml` | False | [Reduce Task > Shuffle](ReduceTask.html#shuffle)
`mapreduce.framework.name` | `mapred-site.xml` | `yarn`/`local` | [Reduce Task > Shuffle](ReduceTask.html#shuffle)
`mapreduce.reduce.shuffle.parallelcopies` | `mapred-site.xml` | 5 | [Reduce Task > Shuffle](ReduceTask.html#shuffle)
`mapreduce.reduce.memory.totalbytes` | `mapred-site.xml` | `Runtime.maxMemory()` | [Reduce Task > Fetcher](ReduceTask.html#local-fetcher)
`mapreduce.reduce.shuffle.memory.limit.percent` | `mapred-site.xml` | 0.25 | [Reduce Task > Fetcher](ReduceTask.html#local-fetcher)
`mapreduce.job.ubertask.enable` | `mapred-site.xml` | False | [Job > NEW => INITED](Job.html#new-inited-job-init)
`mapreduce.job.ubertask.maxmaps` | `mapred-site.xml` | 9 | [Job > NEW => INITED](Job.html#new-inited-job-init)
`mapreduce.job.ubertask.maxreduces` | `mapred-site.xml` | 1 | [Job > NEW => INITED](Job.html#new-inited-job-init)
`mapreduce.job.ubertask.maxbytes` | `mapred-site.xml` | `dfs.block.size` | [Job > NEW => INITED ](Job.html#new-inited-job-init)
`mapreduce.map. failures.maxpercent` | `mapred-site.xml` | 0 | [Job > RUNNING => {RUNNING, COMMITTING, FAIL ABORT}](Job.html#running-running-committing-fail-abort-job-task-completed)
`mapreduce.reduce. failures.maxpercent` | `mapred-site.xml` | 0 | [Job > RUNNING => {RUNNING, COMMITTING, FAIL ABORT}](Job.html#running-running-committing-fail-abort-job-task-completed)
`mapreduce.map.memory.mb` | `mapred-site.xml` | 1024 | [Task Attempt > NEW => UNASSIGNED](TaskAttempt.html#new-unassigned-ta-schedule)
`mapreduce.reduce.memory.mb` | `mapred-site.xml` | 1024 | [Task Attempt > NEW => UNASSIGNED](TaskAttempt.html#new-unassigned-ta-schedule)
`scheduler.maximum-allocation-mb` | `yarn-site.xml` | 8192 | [Container Allocator](ContainerAllocator.html)
`mapreduce.reduce.shuffle.merge.percent` | `mapred-site.xml` | 0.90 | [Reduce Task > Shuffle](ReduceTask.html#shuffle-merge)
`yarn.resourcemanager.scheduler.class` | `yarn-site.xml` | `CapacityScheduler` | [Resource Manager](ResourceManager.html)

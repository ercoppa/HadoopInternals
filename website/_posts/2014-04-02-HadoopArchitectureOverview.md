---
layout: post
title: Hadoop Architecture Overview
---

Apache Hadop is an open-source software framework for storage and large-scale processing of data-sets on clusters of commodity hardware. There are mainly four building blocks inside this runtime enviroment (see figure, from bottom to top):

![Hadoop Architecture Oveview](public/images/hadoop-architecture-oveview_53434015-fd58-4316-a097-39940a00558d.png)

 * the **cluster** is the set of host machines or **nodes** (which may be orginized in subsets of them, called **racks**). This is the hardware part of the infrastructure.
 * the **YARN Infrastructure** is the framework responsible for providing the computational resources (e.g., CPUs, memory, etc.) needed for a program execution. Two important elements are:
   * **Node Manager** (many per cluster) which offers resources and uses them to execute a program related to an application. Each Node Manager typically offers one or more **Container**, an abstraction for one or more resources. Each container is composed by a number of cores and by a specific amount of primary memory.
   * the **Resource Manager** (one per cluster) which runs a **Resource Scheduler** (who assigns Containers to applications) and an **Application Manager** (who tracks the states of all launched applications).
 * the **HDFS Federation** is the framework responsible for providing permanent, reliable and distrubuted storage. This is typically used for storing inputs and output (but not intermediate ones).
 * the **MapReduce Framework** is the software layer implementing the MapReduce paradigm. It is composed by the following elements:
   * the **Application Master** which is responsible for launching computations on assigned resources (by the Resource Manager) and for tracking the state of the application (what has been done, what still needs to be executed) using several *abstract concepts*: a **Job** requires to run several **Tasks**, each one may have one or more **Task Attempt** (an attempt to run it on an assigned container).
   * the **Tasks** (**MapTask** or **ReduceTask**) are two types of computations needed by the *classical* MapReduce paradigm.

The YARN infrastructure and the HDFS federation are completely decoupled and independent: the first one provides resources for running an application while the second one provides storage. The MapReduce framework is only one of many possible framework which runs on top of YARN (although currently is the only one implemented).

### <a href="#hadoop-architecture-s-interactions" id="hadoop-architecture-s-interactions">Hadoop architecture's interactions</a>

![Hadoop Architecture Workflow](public/images/hadoop-architecture-workflow_53302af2-7d38-412b-8275-6ffe0a009433.png)

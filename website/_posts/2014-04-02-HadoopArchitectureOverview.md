---
layout: post
title: Hadoop Architecture Overview
---

Apache Hadop is an open-source software framework for storage and large-scale processing of data-sets on clusters of commodity hardware. There are mainly four building blocks inside this runtime enviroment (see figure, from bottom to top):

![Hadoop Architecture Oveview](public/images/hadoop-architecture-oveview_535fb575-6fcc-4a71-a3c7-71a80a0057dd.png)

 * the **cluster** is the set of host machines or **nodes** (which may be orginized in subsets of them, called **racks**). This is the hardware part of the infrastructure.
 * the **YARN Infrastructure** is the framework responsible for providing the computational resources (e.g., CPUs, memory, etc.) needed for a program execution. Two important elements are:
   * **Node Manager** (many per cluster) which offers resources and uses them to execute a program related to an application. Each Node Manager typically offers one or more **Container**, an abstraction for one or more resources. Each container is composed by a number of cores and by a specific amount of primary memory.
   * the **Resource Manager** (one per cluster) which runs a **Resource Scheduler** (who assigns Containers to applications) and an **Application Manager** (who tracks the states of all launched applications).
 * the **HDFS Federation** is the framework responsible for providing permanent, reliable and distrubuted storage. This is typically used for storing inputs and output (but not intermediate ones).
 * the **MapReduce Framework** is the software layer implementing the MapReduce paradigm. It is composed by the following elements:
   * the **Application Master** which is responsible for launching computations on assigned resources (by the Resource Manager) and for tracking the state of the application (what has been done, what still needs to be executed) using several *abstract concepts*: a **Job** requires to run several **Tasks**, each one may have one or more **Task Attempt** (an attempt to run it on an assigned container).
   * the **Tasks** (**MapTask** or **ReduceTask**) are two types of computations needed by the *classical* MapReduce paradigm.

The YARN infrastructure and the HDFS federation are completely decoupled and independent: the first one provides resources for running an application while the second one provides storage. The MapReduce framework is only one of many possible framework which runs on top of YARN (although currently is the only one implemented).

### <a href="#hadoop-architecture-workflow-interactions" id="hadoop-architecture-workflow-interactions">Hadoop Architecture Workflow (interactions)</a>

The user submits a job using the **Job Submitter** component. This software element connects to the **Resource Manager** and starts their interaction using the *ClientProtocol* and the *ApplicationClientProtocol*. It sends the job configuration and the application jar. Finally, it waits until the job is completed.

The **Resource Manager** when a user submit an application (the job) allocates and starts a new container for an **Application Master**. This component is responsible for the execution of the application according to the MapReduce paradigm. It asks to the **Resource Manager** the containers needed for executing the **MapTasks**. When it obtains them from the **Resource Scheduler**, it starts the execution on the related **Node Managers**. When the majority of the **MapTasks** has been started, it begins to ask more containers for executing the **ReduceTasks**. When almost all **MapTasks** have been completed, it starts the **ReduceTasks**. 

Internally, the **Application Master** tracks the status of an **Application** using the concept of a **Job** which is divided in **Tasks**, each **Task** may have several launched attempts (**Task Attempt**). Each **Task Attempt** is executed on a **Container** of a specific **Node Manager** and it can be a **MapTask** or a **ReduceTask**.

Finally, when all the tasks are completed it notifies the **Resource Manager** which in turn warns the user about the completion of the application.

![Hadoop Architecture Workflow](public/images/hadoop-architecture-workflow_53302af2-7d38-412b-8275-6ffe0a009433.png)

# Hadoop Architecture Overview

[**Apache Hadoop**](http://hadoop.apache.org/) is an open-source software framework for storage and large-scale processing of data-sets on clusters of commodity hardware. There are mainly five building blocks inside this runtime envinroment (from bottom to top):

![Hadoop Architecture Oveview](https://www.lucidchart.com/publicSegments/view/535fb575-6fcc-4a71-a3c7-71a80a0057dd/image.png)

 * the **cluster** is the set of host machines (**nodes**). Nodes may be partitioned in **racks**. This is the hardware part of the infrastructure.
 * the **YARN Infrastructure** (Yet Another Resource Negotiator) is the framework responsible for providing the computational resources (e.g., CPUs, memory, etc.) needed for application executions. Two important elements are:
   * the **Resource Manager** (one per cluster) is the master. It knows where the slaves are located (Rack Awareness) and how many resources they have. It runs several services, the most important is the **Resource Scheduler** which decides how to assign the resources. ![Resource Manager](https://www.lucidchart.com/publicSegments/view/534be06c-eb4c-4516-a178-5ff00a005d90/image.png)


   * the **Node Manager** (many per cluster) is the slave of the infrastructure. When it starts, it announces himself to the Resource Manager. Periodically, it sends an heartbeat to the Resource Manager. Each Node Manager offers some resources to the cluster. Its resource capacity is the amount of memory and the number of vcores. At run-time, the Resource Scheduler will decide how to use this capacity: a **Container** is a fraction of the NM capacity and it is used by the client for running a program. ![Node Manager overview](https://www.lucidchart.com/publicSegments/view/534beb08-0c0c-4d84-bf75-3a670a00c014/image.png)
  
 * the **HDFS Federation** is the framework responsible for providing permanent, reliable and distributed storage. This is typically used for storing inputs and output (but not intermediate ones).
 * other alternative storage solutions. For instance, Amazon uses the Simple Storage Service (S3).
 * the **MapReduce Framework** is the software layer implementing the [MapReduce paradigm](http://en.wikipedia.org/wiki/MapReduce). 

The YARN infrastructure and the HDFS federation are completely decoupled and independent: the first one provides resources for running an application while the second one provides storage. The MapReduce framework is only one of many possible framework which runs on top of YARN (although currently is the only one implemented).

### YARN: Application Startup
![YARN Architecture](https://www.lucidchart.com/publicSegments/view/5356ab97-2bd8-4f19-b30e-1ef60a00dcc0/image.png)

In YARN, there are at least three actors:

 * the **Job Submitter** (the client)
 * the **Resource Manager** (the master)
 * the **Node Manager** (the slave)

The application startup process is the following:

 1. a client submits an application to the Resource Manager
 2. the Resource Manager allocates a container
 3. the Resource Manager contacts the related Node Manager 
 4. the Node Manager launches the container
 5. the Container executes the **Application Master**

![Yarn: Application Startup](https://www.lucidchart.com/publicSegments/view/534bf195-890c-4c7a-95eb-13cb0a008d03/image.png)

The Application Master is responsible for the execution of a single application. It asks for containers to the Resource Scheduler (Resource Manager) and executes specific programs (e.g., the main of a Java class) on the obtained containers. The Application Master knows the application logic and thus it is framework-specific. The MapReduce framework provides its own implementation of an Application Master.

The Resource Manager is a single point of failure in YARN. Using Application Masters, YARN is spreading over the cluster the metadata related to running applications. This reduces the load of the Resource Manager and makes it fast recoverable.

<!--
The user submits a job using the **Job Submitter** component. This software element connects to the **Resource Manager** and starts their interaction using the *ClientProtocol* and the *ApplicationClientProtocol*. It sends the job configuration and the application jar. Finally, it waits until the job is completed.

The **Resource Manager** when a user submit an application (the job) allocates and starts a new container for an **Application Master**. This component is responsible for the execution of the application according to the MapReduce paradigm. It asks to the **Resource Manager** the containers needed for executing the **MapTasks**. When it obtains them from the **Resource Scheduler**, it starts the execution on the related **Node Managers**. When the majority of the **MapTasks** has been started, it begins to ask more containers for executing the **ReduceTasks**. When almost all **MapTasks** have been completed, it starts the **ReduceTasks**. 

Internally, the **Application Master** tracks the status of an **Application** using the concept of a **Job** which is divided in **Tasks**, each **Task** may have several launched attempts (**Task Attempt**). Each **Task Attempt** is executed on a **Container** of a specific **Node Manager** and it can be a **MapTask** or a **ReduceTask**.

Finally, when all the tasks are completed it notifies the **Resource Manager** which in turn warns the user about the completion of the application.

-->

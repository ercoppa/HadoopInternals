---
layout: post
title: Application
---
#### Table of contents:
 * [Finite State Machine](#finite-state-machine)
 * [*NEW => INITTING* [*INIT_APPLICATION*]](#new-initting-init-application)
 * [*NEW => NEW*, *INITTING => INITTING*, *RUNNING => RUNNING* [*INIT_CONTAINER*]](#new-new-initting-initting-running-running-init-container)
 * [*INITTING => INITTING* [*APPLICATION_LOG_HANDLING_INITED*]](#initting-initting-application-log-handling-inited)
 * [*INITTING => RUNNING* [*APPLICATION_INITED*]](#initting-running-application-inited)
 * [*RUNNING => RUNNING* [*APPLICATION_CONTAINER_FINISHED*]](#running-running-application-container-finished)
 * [*RUNNING => {APPLICATION_RESOURCES_CLEAININGUP, APPLICATION_CONTAINERS_WAIT}* [*FINISH_APPLICATION*]](#running-application-resources-cleainingup-application-containers-wait-finish-application)
 * [*FINISHING_CONTAINERS_WAIT => {APPLICATION_CONTAINER_FINISHED, APPLICATION_RESOURCES_CLEANINGUP} * [*APPLICATION_CONTAINER_FINISHED*]](#finishing-containers-wait-application-container-finished-application-resources-cleaningup-application-container-finished)

### <a href="#finite-state-machine" id="finite-state-machine">Finite State Machine</a>
![Hadoop (MapReduce): Application - Finite State Machine](public/images/hadoop-mapreduce-application-finite-state-machine_53304bf7-2904-481c-9a7a-3f890a00da32.png)

### <a href="#new-initting-init-application" id="new-initting-init-application">*NEW => INITTING* [*INIT_APPLICATION*]</a>
![Hadoop (MapReduce): Application - NEW => INITTING - INIT_APPLICATION](public/images/hadoop-mapreduce-application-new-initting-init-application_53304c35-a748-499c-bce7-25910a004cb7.png)

### <a href="#new-new-initting-initting-running-running-init-container" id="new-new-initting-initting-running-running-init-container">*NEW => NEW*, *INITTING => INITTING*, *RUNNING => RUNNING* [*INIT_CONTAINER*]</a>
![Hadoop (MapReduce): Application - NEW => NEW - INIT_CONTAINER](public/images/hadoop-mapreduce-application-new-new-init-container_53304cde-0c94-44a3-a7b4-3fc60a00da32.png)

### <a href="#initting-initting-application-log-handling-inited" id="initting-initting-application-log-handling-inited">*INITTING => INITTING* [*APPLICATION_LOG_HANDLING_INITED*]</a>
![Hadoop (MapReduce): Application - INITTING => INITTING - APPLICATION_LOG_HANDLING_INITED](public/images/hadoop-mapreduce-application-initting-initting-application-log-handling-inited_53304d5d-529c-4546-8ac2-74ad0a00d013.png)

### <a href="#initting-running-application-inited" id="initting-running-application-inited">*INITTING => RUNNING* [*APPLICATION_INITED*]</a>
![Hadoop (MapReduce): Application - INITTING => RUNNING - APPLICATION_INITED](public/images/hadoop-mapreduce-application-initting-running-application-inited_53304daf-0028-42c5-b080-2ab30a004cb7.png)

### <a href="#running-running-application-container-finished" id="running-running-application-container-finished">*RUNNING => RUNNING* [*APPLICATION_CONTAINER_FINISHED*]</a>
![Hadoop (MapReduce): Application - RUNNING => RUNNING - APPLICATION_CONTAINER_FINISHED](public/images/hadoop-mapreduce-application-running-running-application-container-finished_53304dfa-5658-408d-a013-15510a00da32.png)

### <a href="#running-application-resources-cleainingup-application-containers-wait-finish-application" id="running-application-resources-cleainingup-application-containers-wait-finish-application">*RUNNING => {APPLICATION_RESOURCES_CLEAININGUP, APPLICATION_CONTAINERS_WAIT}* [*FINISH_APPLICATION*]</a>
![Hadoop (MapReduce): Application - RUNNING => {APPLICATION_RESOURCES_CLEAININGUP, APPLICATION_CONTAINERS_WAIT} - FINISH_APPLICATION](public/images/hadoop-mapreduce-application-running-application-resources-cleainingup-application-containers-wait-finish-application_53304ece-c78c-4b7d-b0fb-039e0a00d013.png)

### <a href="#finishing-containers-wait-application-container-finished-application-resources-cleaningup-application-container-finished" id="finishing-containers-wait-application-container-finished-application-resources-cleaningup-application-container-finished">*FINISHING_CONTAINERS_WAIT => {APPLICATION_CONTAINER_FINISHED, APPLICATION_RESOURCES_CLEANINGUP} * [*APPLICATION_CONTAINER_FINISHED*]</a>
![Hadoop (MapReduce): Application - FINISHING_CONTAINERS_WAIT => {APPLICATION_CONTAINER_FINISHED, APPLICATION_RESOURCES_CLEANINGUP} - APPLICATION_CONTAINER_FINISHED](public/images/hadoop-mapreduce-application-finishing-containers-wait-application-container-finished-application-resources-cleaningup-application-container-finished_53304f82-e294-4565-9eb8-21eb0a00da32.png)

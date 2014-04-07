# Application
[toc]

### Finite State Machine
![Hadoop (MapReduce): Application - Finite State Machine](https://www.lucidchart.com/publicSegments/view/53304bf7-2904-481c-9a7a-3f890a00da32/image.png)

### *NEW => INITTING* [*INIT_APPLICATION*]
![Hadoop (MapReduce): Application - NEW => INITTING - INIT_APPLICATION](https://www.lucidchart.com/publicSegments/view/53304c35-a748-499c-bce7-25910a004cb7/image.png)

### *NEW => NEW*, *INITTING => INITTING*, *RUNNING => RUNNING* [*INIT_CONTAINER*]
![Hadoop (MapReduce): Application - NEW => NEW - INIT_CONTAINER](https://www.lucidchart.com/publicSegments/view/53304cde-0c94-44a3-a7b4-3fc60a00da32/image.png)

### *INITTING => INITTING* [*APPLICATION_LOG_HANDLING_INITED*]
![Hadoop (MapReduce): Application - INITTING => INITTING - APPLICATION_LOG_HANDLING_INITED](https://www.lucidchart.com/publicSegments/view/53304d5d-529c-4546-8ac2-74ad0a00d013/image.png)

### *INITTING => RUNNING* [*APPLICATION_INITED*]
![Hadoop (MapReduce): Application - INITTING => RUNNING - APPLICATION_INITED](https://www.lucidchart.com/publicSegments/view/53304daf-0028-42c5-b080-2ab30a004cb7/image.png)

### *RUNNING => RUNNING* [*APPLICATION_CONTAINER_FINISHED*]
![Hadoop (MapReduce): Application - RUNNING => RUNNING - APPLICATION_CONTAINER_FINISHED](https://www.lucidchart.com/publicSegments/view/53304dfa-5658-408d-a013-15510a00da32/image.png)

### *RUNNING => {APPLICATION_RESOURCES_CLEAININGUP, APPLICATION_CONTAINERS_WAIT}* [*FINISH_APPLICATION*]
![Hadoop (MapReduce): Application - RUNNING => {APPLICATION_RESOURCES_CLEAININGUP, APPLICATION_CONTAINERS_WAIT} - FINISH_APPLICATION](https://www.lucidchart.com/publicSegments/view/53304ece-c78c-4b7d-b0fb-039e0a00d013/image.png)

### *FINISHING_CONTAINERS_WAIT => {APPLICATION_CONTAINER_FINISHED, APPLICATION_RESOURCES_CLEANINGUP} * [*APPLICATION_CONTAINER_FINISHED*]
![Hadoop (MapReduce): Application - FINISHING_CONTAINERS_WAIT => {APPLICATION_CONTAINER_FINISHED, APPLICATION_RESOURCES_CLEANINGUP} - APPLICATION_CONTAINER_FINISHED](https://www.lucidchart.com/publicSegments/view/53304f82-e294-4565-9eb8-21eb0a00da32/image.png)

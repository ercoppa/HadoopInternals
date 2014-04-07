### Task Attempt
[toc]

### Finite State Machine
![Hadoop (MapReduce): Task Attempt - Finite State Machine](https://www.lucidchart.com/publicSegments/view/5330591e-64f4-49d1-a118-54e30a004cb7/image.png)

### *NEW => UNASSIGNED* [*TA_SCHEDULE*]
![Hadoop (MapReduce): Task Attempt - NEW => UNASSIGNED - TA_SCHEDULE](https://www.lucidchart.com/publicSegments/view/53305997-5638-43c0-92e2-018c0a00da32/image.png)

### *UNASSIGNED => ASSIGNED* [*TA_ASSIGNED*]
![Hadoop (MapReduce): Task Attempt - UNASSIGNED => ASSIGNED - TA_ASSIGNED](https://www.lucidchart.com/publicSegments/view/533059e9-9d18-4042-aae5-4ffe0a00da8d/image.png)

### *ASSIGNED => RUNNING* [*TA_CONTAINER_LAUNCHED*]
![Hadoop (MapReduce): Task Attempt - ASSIGNED => RUNNING - TA_CONTAINER_LAUNCHED](https://www.lucidchart.com/publicSegments/view/53305a1a-1d10-4811-889d-2df60a00d013/image.png)

### *RUNNING => SUCCESS_CONTAINER_CLEANUP* [*TA_DONE*], *COMMIT_PENDING => SUCCESS_CONTAINER_CLEANUP* [*TA_DONE*]
![Hadoop (MapReduce): Task Attempt - RUNNING => SUCCESS_CONTAINER_CLEANUP - TA_DONE - COMMIT_PENDING => SUCCESS_CONTAINER_CLEANUP](https://www.lucidchart.com/publicSegments/view/53305ad5-8d54-460e-893a-3a880a004683/image.png) 

### *SUCCESS_CONTAINER_CLEANUP => SUCCEEDEED* [*TA_CONTAINER_CLEANED*]
![Hadoop (MapReduce): Task Attempt - SUCCESS_CONTAINER_CLEANUP => SUCCEEDEED - TA_CONTAINER_CLEANED](https://www.lucidchart.com/publicSegments/view/53305b06-4494-41e6-8baf-42c90a009b9f/image.png)

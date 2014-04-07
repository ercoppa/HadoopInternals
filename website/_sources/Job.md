### Job 
[toc]

### Finite State Machine
![Hadoop (MapReduce): Job - Finite State Machine](https://www.lucidchart.com/publicSegments/view/5330528e-f8fc-47c3-a285-3b170a004683/image.png)

### *NEW => INITED* [*JOB_INIT*]
![Hadoop (MapReduce): Job - NEW => INITED - JOB_INIT](https://www.lucidchart.com/publicSegments/view/533052cd-e434-4013-a881-31b60a00da32/image.png)

### *INITTED => SETUP* [*JOB_START*]
![Hadoop (MapReduce): Job - INITTED => SETUP - JOB_START](https://www.lucidchart.com/publicSegments/view/53305310-d370-491c-b842-2f320a009433/image.png)

### *SETUP => RUNNING* [*JOB_SETUP_COMPLETED*]
![Hadoop (MapReduce): Job - SETUP => RUNNING - JOB_SETUP_COMPLETED](https://www.lucidchart.com/publicSegments/view/53305392-374c-4ab6-ab2a-7f660a009433/image.png)

### *RUNNING => {RUNNING, COMMITTING, FAIL ABORT}* [*JOB_TASK_COMPLETED*]
![Hadoop (MapReduce): Job - RUNNING => RUNNING, COMMITTING, FAIL ABORT - JOB_TASK_COMPLETED](https://www.lucidchart.com/publicSegments/view/53305441-e19c-455d-9571-125a0a00da32/image.png)

### *RUNNING => RUNNING* [*JOB_TASK_ATTEMPT_COMPLETED*]
![Hadoop (MapReduce): Job - RUNNING => RUNNING - JOB_TASK_ATTEMPT_COMPLETED](https://www.lucidchart.com/publicSegments/view/53305406-7c44-463e-a456-33740a004cb7/image.png)

### *COMMITTING => SUCCEEDED* [*JOB_COMMIT_COMPLETED*]
![Hadoop (MapReduce): Job - COMMITTED => SUCCEEDED - JOB_COMMIT_COMPLETED](https://www.lucidchart.com/publicSegments/view/53300917-07ac-4950-aa31-29d90a004cb7/image.png)

Apache Hadoop (MapReduce): Job 
==============
#### Table of contents:
 * [Finite State Machine](#finite-state-machine) 
 * [*NEW => INITED*](#transition-new--inited)
 * [*INITTED => SETUP*](#transitions-initted--setup-setup--running-running--running-committing-fail-abort-running--running)
 * [*SETUP => RUNNING*](#transitions-initted--setup-setup--running-running--running-committing-fail-abort-running--running)
 * [*RUNNING => RUNNING*](#transitions-initted--setup-setup--running-running--running-committing-fail-abort-running--running)
 * [*RUNNING => {RUNNING, COMMITTING, FAIL ABORT}*](#transitions-initted--setup-setup--running-running--running-committing-fail-abort-running--running)
 * [*COMMITTING => SUCCEEDED*](#transition-committing--succeeded)

### Finite State Machine
<a>![](sources/png/Yarn_(5)_-_Job_Execution_FSM_(1).png)</a>

### Transition: *NEW => INITED* 
<a>![](sources/png/Yarn_(6)_-_Job_execution_(1).png)</a>

### Transitions: *INITTED => SETUP*, *SETUP => RUNNING*, *RUNNING => {RUNNING, COMMITTING, FAIL ABORT}, *RUNNING => RUNNING*
<a>![](sources/png/Yarn_(7)_-_Job_Execution_(2).png)</a>

### Transition: *COMMITTING => SUCCEEDED*
<a>![](sources/png/Yarn_(8)_-_Job_Execution_(3).png)</a>

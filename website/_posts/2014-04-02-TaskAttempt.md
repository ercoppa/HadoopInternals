---
layout: post
title: Task Attempt
---
#### Table of contents:
 * [Finite State Machine](#finite-state-machine)
 * [*NEW => UNASSIGNED* [*TA_SCHEDULE*]](#new-unassigned-ta-schedule)
 * [*UNASSIGNED => ASSIGNED* [*TA_ASSIGNED*]](#unassigned-assigned-ta-assigned)
 * [*ASSIGNED => RUNNING* [*TA_CONTAINER_LAUNCHED*]](#assigned-running-ta-container-launched)
 * [*RUNNING => SUCCESS_CONTAINER_CLEANUP* [*TA_DONE*], *COMMIT_PENDING => SUCCESS_CONTAINER_CLEANUP* [*TA_DONE*]](#running-success-container-cleanup-ta-done-commit-pending-success-container-cleanup-ta-done)
 * [*SUCCESS_CONTAINER_CLEANUP => SUCCEEDEED* [*TA_CONTAINER_CLEANED*]](#success-container-cleanup-succeedeed-ta-container-cleaned)

### <a href="#finite-state-machine" id="finite-state-machine">Finite State Machine</a>
![Hadoop (MapReduce): Task Attempt - Finite State Machine](public/images/hadoop-mapreduce-task-attempt-finite-state-machine_5330591e-64f4-49d1-a118-54e30a004cb7.png)

### <a href="#new-unassigned-ta-schedule" id="new-unassigned-ta-schedule">*NEW => UNASSIGNED* [*TA_SCHEDULE*]</a>
![Hadoop (MapReduce): Task Attempt - NEW => UNASSIGNED - TA_SCHEDULE](public/images/hadoop-mapreduce-task-attempt-new-unassigned-ta-schedule_53305997-5638-43c0-92e2-018c0a00da32.png)

### <a href="#unassigned-assigned-ta-assigned" id="unassigned-assigned-ta-assigned">*UNASSIGNED => ASSIGNED* [*TA_ASSIGNED*]</a>
![Hadoop (MapReduce): Task Attempt - UNASSIGNED => ASSIGNED - TA_ASSIGNED](public/images/hadoop-mapreduce-task-attempt-unassigned-assigned-ta-assigned_533059e9-9d18-4042-aae5-4ffe0a00da8d.png)

### <a href="#assigned-running-ta-container-launched" id="assigned-running-ta-container-launched">*ASSIGNED => RUNNING* [*TA_CONTAINER_LAUNCHED*]</a>
![Hadoop (MapReduce): Task Attempt - ASSIGNED => RUNNING - TA_CONTAINER_LAUNCHED](public/images/hadoop-mapreduce-task-attempt-assigned-running-ta-container-launched_53305a1a-1d10-4811-889d-2df60a00d013.png)

### <a href="#running-success-container-cleanup-ta-done-commit-pending-success-container-cleanup-ta-done" id="running-success-container-cleanup-ta-done-commit-pending-success-container-cleanup-ta-done">*RUNNING => SUCCESS_CONTAINER_CLEANUP* [*TA_DONE*], *COMMIT_PENDING => SUCCESS_CONTAINER_CLEANUP* [*TA_DONE*]</a>
![Hadoop (MapReduce): Task Attempt - RUNNING => SUCCESS_CONTAINER_CLEANUP - TA_DONE - COMMIT_PENDING => SUCCESS_CONTAINER_CLEANUP](public/images/hadoop-mapreduce-task-attempt-running-success-container-cleanup-ta-done-commit-pending-success-container-cleanup_53305ad5-8d54-460e-893a-3a880a004683.png) 

### <a href="#success-container-cleanup-succeedeed-ta-container-cleaned" id="success-container-cleanup-succeedeed-ta-container-cleaned">*SUCCESS_CONTAINER_CLEANUP => SUCCEEDEED* [*TA_CONTAINER_CLEANED*]</a>
![Hadoop (MapReduce): Task Attempt - SUCCESS_CONTAINER_CLEANUP => SUCCEEDEED - TA_CONTAINER_CLEANED](public/images/hadoop-mapreduce-task-attempt-success-container-cleanup-succeedeed-ta-container-cleaned_53305b06-4494-41e6-8baf-42c90a009b9f.png)

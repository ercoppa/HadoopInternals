---
layout: post
title: Container
---
#### Table of contents:
 * [Finite State Machine](#finite-state-machine)
 * [*NEW => {LOCALIZED; LOCALIZING, LOCALIZATION_FAILED}* [*INIT_CONTAINER*]](#new-localized-localizing-localization-failed-init-container)
 * [*LOCALIZING => {LOCALIZING, LOCALIZED}* [*RESOURCE_LOCALIZED*]](#localizing-localizing-localized-resource-localized)
 * [*LOCALIZED => RUNNING* [*CONTAINER_LAUNCHED*]](#localized-running-container-launched)
 * [*RUNNING => EXITED_WITH_SUCCESS* [*CONTAINER_EXITED_WITH_SUCCESS*]](#running-exited-with-success-container-exited-with-success)
 * [*EXITED_WITH_SUCCESS => DONE* [*CONTAINER_RESOURCES_CLEANEDUP*]](#exited-with-success-done-container-resources-cleanedup)

### <a href="#finite-state-machine" id="finite-state-machine">Finite State Machine</a>
![Hadoop (MapReduce): Container - Finite State Machine](public/images/hadoop-mapreduce-container-finite-state-machine_53305c19-5c74-4f55-bba8-01b60a00da32.png)

### <a href="#new-localized-localizing-localization-failed-init-container" id="new-localized-localizing-localization-failed-init-container">*NEW => {LOCALIZED; LOCALIZING, LOCALIZATION_FAILED}* [*INIT_CONTAINER*]</a>
![Hadoop (MapReduce): Container - NEW => {LOCALIZED; LOCALIZING, LOCALIZATION_FAILED} - INIT_CONTAINER](public/images/hadoop-mapreduce-container-new-localized-localizing-localization-failed-init-container_53305c9a-b260-4b62-b3c3-017d0a00da32.png)

### <a href="#localizing-localizing-localized-resource-localized" id="localizing-localizing-localized-resource-localized">*LOCALIZING => {LOCALIZING, LOCALIZED}* [*RESOURCE_LOCALIZED*]</a>
![Hadoop (MapReduce): Container - LOCALIZING => {LOCALIZING, LOCALIZED} - RESOURCE_LOCALIZED](public/images/hadoop-mapreduce-container-localizing-localizing-localized-resource-localized_53305cc0-1b2c-4212-ab2a-3e890a00d013.png)

### <a href="#localized-running-container-launched" id="localized-running-container-launched">*LOCALIZED => RUNNING* [*CONTAINER_LAUNCHED*]</a>
![Hadoop (MapReduce): Container - LOCALIZED => RUNNING - CONTAINER_LAUNCHED](public/images/hadoop-mapreduce-container-localized-running-container-launched_53305d0e-1d28-408f-abea-742f0a004cb7.png)

### <a href="#running-exited-with-success-container-exited-with-success" id="running-exited-with-success-container-exited-with-success">*RUNNING => EXITED_WITH_SUCCESS* [*CONTAINER_EXITED_WITH_SUCCESS*]</a>
![Hadoop (MapReduce): Container - RUNNING => EXITED_WITH_SUCCESS - CONTAINER_EXITED_WITH_SUCCESS](public/images/hadoop-mapreduce-container-running-exited-with-success-container-exited-with-success_53305d4e-7d3c-47bc-9535-5dfd0a009107.png)

### <a href="#exited-with-success-done-container-resources-cleanedup" id="exited-with-success-done-container-resources-cleanedup">*EXITED_WITH_SUCCESS => DONE* [*CONTAINER_RESOURCES_CLEANEDUP*]</a>
![Hadoop (MapReduce): Container - EXITED_WITH_SUCCESS => DONE - CONTAINER_RESOURCES_CLEANEDUP](public/images/hadoop-mapreduce-container-exited-with-success-done-container-resources-cleanedup_53305d94-593c-4bed-ab56-297f0a00da8d.png)

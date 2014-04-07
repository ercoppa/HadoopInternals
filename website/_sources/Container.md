### Container
[toc]

### Finite State Machine
![Hadoop (MapReduce): Container - Finite State Machine](https://www.lucidchart.com/publicSegments/view/53305c19-5c74-4f55-bba8-01b60a00da32/image.png)

### *NEW => {LOCALIZED; LOCALIZING, LOCALIZATION_FAILED}* [*INIT_CONTAINER*]
![Hadoop (MapReduce): Container - NEW => {LOCALIZED; LOCALIZING, LOCALIZATION_FAILED} - INIT_CONTAINER](https://www.lucidchart.com/publicSegments/view/53305c9a-b260-4b62-b3c3-017d0a00da32/image.png)

### *LOCALIZING => {LOCALIZING, LOCALIZED}* [*RESOURCE_LOCALIZED*]
![Hadoop (MapReduce): Container - LOCALIZING => {LOCALIZING, LOCALIZED} - RESOURCE_LOCALIZED](https://www.lucidchart.com/publicSegments/view/53305cc0-1b2c-4212-ab2a-3e890a00d013/image.png)

### *LOCALIZED => RUNNING* [*CONTAINER_LAUNCHED*]
![Hadoop (MapReduce): Container - LOCALIZED => RUNNING - CONTAINER_LAUNCHED](https://www.lucidchart.com/publicSegments/view/53305d0e-1d28-408f-abea-742f0a004cb7/image.png)

### *RUNNING => EXITED_WITH_SUCCESS* [*CONTAINER_EXITED_WITH_SUCCESS*]
![Hadoop (MapReduce): Container - RUNNING => EXITED_WITH_SUCCESS - CONTAINER_EXITED_WITH_SUCCESS](https://www.lucidchart.com/publicSegments/view/53305d4e-7d3c-47bc-9535-5dfd0a009107/image.png)

### *EXITED_WITH_SUCCESS => DONE* [*CONTAINER_RESOURCES_CLEANEDUP*]
![Hadoop (MapReduce): Container - EXITED_WITH_SUCCESS => DONE - CONTAINER_RESOURCES_CLEANEDUP](https://www.lucidchart.com/publicSegments/view/53305d94-593c-4bed-ab56-297f0a00da8d/image.png)

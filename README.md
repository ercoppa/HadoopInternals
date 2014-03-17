HadoopDiagrams
==============

This project contains several diagrams describing [Apache Hadoop](http://hadoop.apache.org/) internals (2.3.0 or later). Even if these diagrams are **NOT** specified in any formal or unambiguous language (e.g., UML), they should be reasonably understandable and useful for any person who want to grasp the main ideas behind Hadoop. Unfortunately, not all the internal details are covered by these diagrams. You are free to help :)

This document is an easy-index of all the diagrams. In the source directory, you can find the diagram's sources in the following formats:
* PNG
* Visio (VDX)

A VDX file can be opened with many VISIO editors (e.g., I am using the web-application editor [LucidChart](www.lucidchart.com) but unfortunately only pro users can edit an imported file). If requested, I can share LucicChart files using Google Drive and you can help me in this project (in this case, the free account on LucidChart is enough for editing). 

#### Table of contents:
* [Diagram notational conventions](#diagram-notational-conventions)
* [Job](Job.md)
 * [Finite State Machine](JOB.md#finite-state-machine) 
 * [*NEW => INITED*](JOB.md#transition-new--inited)
 * [*INITTED => SETUP*](JOB.md#transitions-initted--setup-setup--running-running--running-committing-fail-abort-running--running)
 * [*SETUP => RUNNING*](JOB.md#transitions-initted--setup-setup--running-running--running-committing-fail-abort-running--running)
 * [*RUNNING => RUNNING*](JOB.md#transitions-initted--setup-setup--running-running--running-committing-fail-abort-running--running)
 * [*RUNNING => {RUNNING, COMMITTING, FAIL ABORT}*](JOB.md#transitions-initted--setup-setup--running-running--running-committing-fail-abort-running--running)
 * [*COMMITTING => SUCCEEDED*](JOB.md#transition-committing--succeeded)
* Task
* Task Attempt
* NodeManager
* ResourceManager
* ApplicationMaster

### Diagram notational conventions

The style of the diagrams is not very strict and formal but these are some conventions:


<a>![](https://github.com/ercoppa/HadoopDiagrams/raw/master/extra/conventions-1.png)</a> | <a>![](https://github.com/ercoppa/HadoopDiagrams/raw/master/extra/conventions-3.png)</a>
------------ | ------------- 
<a>![](https://github.com/ercoppa/HadoopDiagrams/raw/master/extra/conventions-2.png)</a> |  <a>![](https://github.com/ercoppa/HadoopDiagrams/raw/master/extra/conventions-4.png)</a>


<!---

<a>![](https://github.com/ercoppa/HadoopDiagrams/raw/master/sources/png/MapReduce%20Input.png)</a>
-->

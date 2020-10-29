:orphan:

Hermes
======

Project Abstract
-----------------

Hermes is a hypervisor for MCU-based systems with real-time requirements. The goal of Hermes is to manage tradeoffs between performance and flexibility in software that runs on embedded systems. Bare-metal software often has the best performance—low I/O latency, less CPU and memory overhead, etc. RTOS-based software has comparatively higher flexibility in terms of its ability to share resources and manage multiple jobs but often sacrifices latency. Hermes aims to provide software developers with the option to run some portions of code in a bare-metal environment with minimal latency while allowing other jobs to run within a more flexible RTOS.

Simply Put
----------
In this project, we're building virtualization tools for mobile and IoT systems. Think of it like VMWare for your phone. Apps can run inside isolated virtual machines so they can't snoop on your personal data, and the virtualization software can be installed by anyone---you don't need to root your phone for Hermes to work.

Website
-------

http://hermes.cs.luc.edu

Key Papers
----------

.. todo:: Neil to put these papers up on eCommons.

Neil Klingensmith and Suman Banerjee, *Using Virtualized Task Isolation to Improve Responsiveness in Mobile and IoT Software*, ACM IoTDI, Montreal, QC, CA, April 2019

Neil Klingensmith and Suman Banerjee, *A Hypervisor-Based Privacy Agent for Mobile and IoT Systems*, ACM HotMobile, Santa Cruz, CA, February 2019

Neil Klingensmith and Suman Banerjee, *Hermes: A Real Time Hypervisor for Mobile and IoT Systems*, ACM HotMobile, Tempe, AZ, February 2018

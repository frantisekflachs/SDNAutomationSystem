SDN Automation System
=====================
*The right way how to teach SDN technology easily

### What is SDN Automation System?
The SDN Automation System automates the start of the topology according to defined parameters and then tests the configuration. The advantage is easy extensibility and implementation of other SDN controllers and test sets for practical assignments.

### How does it work?
The SDN Automation System installs the required SDN controller of choice in the application GUI and links it to the created virtual devices in the [Mininet Project](http://mininet.org). The SDN controller runs as a standalone process, which is connected to the switch via OpenFlow protocol. The switches are connected to emulated guests using virtual ethernet pairs.

### Introduction
This thesis deals with the design and implementation of an automated system for networkdevice configuration. The system consists of several main components, which are interfacesfor communicating with SDN controllers, interfaces for communicating with a virtual ne-twork, and a set of network device configuration tests, including a tool that performs them.The automated system is based on a model-view-controller software architecture. Scalabi-lity is provided by adding instances of SDN controllers that can then be linked to a virtualnetwork. The system is designed for network education academies to teach software-definednetworks. For learning purposes, the system is designed to automatically run the requirednetwork controller, virtual network with defined parameters, including the OpenFlow proto-col version, and to run a set of defined tests on a selected topology. After running the tests,the student receives feedback to correct or change the configuration.

### Documentation

### Installation

### Launch
`python3.7 main.py`

### Verified environments
  - [Ubuntu 18.04 LTS](https://www.ubuntu.cz/)
  - [Python 3.7](https://www.python.org/)
  - [Onos 1.15.0](https://wiki.onosproject.org/)
  - [OpenDaylight xx](https://www.opendaylight.org/)
  - [Floodlight 1.2](https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/overview)
  - [Pox eel](https://noxrepo.github.io/pox-doc/html/)
  - [Ryu 4.34](https://osrg.github.io/ryu/)

### Join project
SDN Automation System is open-source and is currently hosted at <https://github.com/frantisekflachs/SDNAutomationSystem>.  You are encouraged to download the code, examine it, modify it, and submit bug reports, bug fixes, feature requests, new features and other issues and pull requests.
# MECH3433_Task1

---
<!-- TOC -->
* [MECH3433_Task1](#mech3433_task1)
  * [Work Division](#work-division)
  * [Python and Robomaster SDK config](#python-and-robomaster-sdk-config)
    * [Important points:](#important-points)
<!-- TOC -->

---
## Work Division
	- Shooter robot
		- detect finished tower
		- predict the target motion and shoot the target while it is moving
	- Builder
		- detect building blocks and stacking sequence
		- detect build location
		- move and place building blocks
##  Python and Robomaster SDK config

---

### Important points:
* Robomaster SDK only works for python 3.8 or below, python 3.9+ ***WILL NOT WORK***
  * Python 3.8.10 installer link [**HERE**](https://www.python.org/downloads/release/python-3810/)

After Python 3.8.10 is installed, please run ```pip intstall robomaster``` to install the robomaster SDK.

If you would like to do it within pycharm, please run ```py -m pip install robomaster``` within the terminal tab.

Please create a new branch from ```origin:main``` to keep track of your own changes and refrain from merging to ```origin:main``` without testing.

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

---

##  Robomaster connection method

  There are a few methods to connect the robomaster to the controlling laptop.
  
* **Wi-Fi Direct** connection with robomaster in AP mode (single robomaster only)
* **Wi-Fi** connection with the laptop in AP mode (multiple robomasters)

~~As we plan to use multiple robomasters together, we should use a laptop as the AP and connect all the robomasters to it.~~

**Robomaster S1 DOES NOT SUPPORT PYTHON SDK**

##		Completed Code

	Only the files main.py, distance.py and robot_grip_v2.py is used for task 4.

## MECH3433_TaskA4_Sequence
Building the tower in correct sequence under the rule of Hanoi Tower using sequence.py

# DiscreteControlsGroup

## Overview

This package is used to simulate a UGV in ROS/Gazebo

## Packages Needed
- Python 2.7
- ROS Indigo (Might work in Kinetic)

## Setup Bashrc File
```
$ sudo gedit ~/.bashrc

# Paste the following lines at the bottom of the file

export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:/home/<username>/catkin_ws/src
source /home/<username>/catkin_ws/devel/setup.bash

```

### If you have permissions errors
```
$ roscd DiscreteControlsGroup
$ cd ..
$ sudo chmod -R 777 DiscreteControlsGroup
```

## How to Run with viewing in Gazebo
```
$ roscore
$ roslaunch DiscreteControlsGroup empty_world.launch 
$ rosrun DiscreteControlsGroup ugv.py

```






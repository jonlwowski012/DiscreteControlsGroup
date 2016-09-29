#!/usr/bin/env python

# Quadrotor Simulator
# Jonathan Lwowski 
# Email: jonathan.lwowski@gmail.com
# Unmanned Systems Lab
# The University of Texas at San Antonio


#########          Libraries         ###################
import sys
import rospy
import math
import time
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseArray


###### Global Variables   #####################
ugv_location = []


### Callback for UGV Pose and Orientation stored into global ROS Geometry Pose class ###
def ugvCallback(data):
	global ugv_location
	for i in range(len(data.name)):
		if "p3dx" in data.name[i]:
			ugv_location = data.pose[i]

### Subscribe for UGV Position and Orientation  (ROS Geometry Pose Msg) ####
def ugv_location_sub():
	rospy.Subscriber("/gazebo/model_states", ModelStates, ugvCallback)  
   
  
###### Function to control ugv. Use Linear X and angular Z   #######
def set_velocity_ugv(lx1, ly1, lz1, ax1, ay1, az1):   
    pub1 = rospy.Publisher('/p3dx/cmd_vel', Twist, queue_size=10)
    r = rospy.Rate(10) # 10hz
    command1 = Twist()
    command1.linear.x = lx1
    command1.linear.y = ly1
    command1.linear.z = lz1
    command1.angular.x = ax1
    command1.angular.y = ay1
    command1.angular.z = az1
    pub1.publish(command1)
         


###### This Function Should move robot from current pose to desired pose   #####
def goto_target(x,y):
	#### Insert Controller Here in place of two lines below  #####
	while(1):
		set_velocity_ugv(.5, 0, 0, 0, 0, 1.0)

	

if __name__ == '__main__':
	### Rospy Init ####
	rospy.init_node('ugv_ros', anonymous=True)
	
	### Subscribe to UGV Location  ###
	ugv_location_sub()
	
	try:
		goto_target(5,5)

		
	except rospy.ROSInterruptException: pass

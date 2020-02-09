#!/usr/bin/env python

import sys
import rospy
from turtlesim_numbers_msgs.srv import TurtleSim_Numbers_Service, TurtleSim_Numbers_ServiceRequest
x=0
def main():
    rospy.init_node('numbers_client')
    rospy.wait_for_service('numbers')
    numbers = rospy.ServiceProxy('numbers', TurtleSim_Numbers_Service)
    x = int(input("Enter Number : "))  
    req=TurtleSim_Numbers_ServiceRequest(x)
    response=numbers(req)
    print "Requesting %s"%(x)
    return response

if __name__ == "__main__":
	main()

#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def linear_motion():

    rospy.init_node('linear_motion', anonymous=False)

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

    rate = rospy.Rate(10)

    twist = Twist()

    twist.linear.x = 0.3

    twist.angular.z = 0

    while not rospy.is_shutdown():

        pub.publish(twist)

        rate.sleep()

if __name__ == "__main__":
    try:
        linear_motion()
    except rospy.ROSInterruptException:
        pass


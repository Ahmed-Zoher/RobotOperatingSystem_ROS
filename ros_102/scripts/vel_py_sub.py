#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def functionCb(msg):
    rospy.loginfo("Linear Components are: %f %f %f",msg.linear.x,msg.linear.y,msg.linear.z)
    rospy.loginfo("Angular Components are: %f %f %f",msg.angular.x,msg.angular.y,msg.angular.z)

def subscriber():
    rospy.init_node('node_2', anonymous=False)
    rospy.Subscriber('/topic_1', Twist, functionCb)
  

    rospy.spin()

if __name__== '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass

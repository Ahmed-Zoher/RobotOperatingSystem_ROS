#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def functionCb(msg):
    rospy.loginfo("Received msg from /topic_1 is: %s", msg.data)

def functionCb2(msg):
    rospy.loginfo("Received msg from /topic_2 is: %s", msg.data)

def subscriber():
    rospy.init_node('node_2', anonymous=False)
    rospy.Subscriber('/topic_1', String, functionCb)
    rospy.Subscriber('/topic_2', String, functionCb2)

    rospy.spin()

if __name__== '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass

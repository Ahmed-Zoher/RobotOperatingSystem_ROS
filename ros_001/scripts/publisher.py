#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def simplePublisher():
    pub = rospy.Publisher('/topic_1', String, queue_size=5)
    pub_2 = rospy.Publisher('/topic_2', String, queue_size=5)
    rospy.init_node('node_1', anonymous=False)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        pub.publish("my first ROS topic")
        pub.publish("message 2")
        pub_2.publish("message from python topic_2")
        rate.sleep()    # 500msec

if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass

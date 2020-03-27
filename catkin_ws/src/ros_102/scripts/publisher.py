#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def simplePublisher():
    pub = rospy.Publisher('/topic_1', String, queue_size=5)
    rospy.init_node('node_1', anonymous=True)
    rate = rospy.Rate(2) # 2hz
    i=-1
    while not rospy.is_shutdown():
        pub.publish(str(i))
	i=i+1
        rate.sleep()    # 500msec
        if (i == 11):
		i=0

if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass

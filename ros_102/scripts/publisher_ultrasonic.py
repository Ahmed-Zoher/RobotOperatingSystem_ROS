#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def simplePublisher():
    pub = rospy.Publisher('/sensor/ultrasonic', String, queue_size=5)
    rospy.init_node('node_1', anonymous=True)
    rate = rospy.Rate(0.5) # 2hz
    i=105
    while not rospy.is_shutdown():
        pub.publish(str(i))
	i=i-5
        rate.sleep()    # 500msec
        if (i == -5):
		i=100

if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass

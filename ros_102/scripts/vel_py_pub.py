#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def simplePublisher():
    pub = rospy.Publisher('/topic_1', Twist, queue_size=7)
  
    rospy.init_node('node_1', anonymous=False)
    rate = rospy.Rate(1) # 1hz
    msg=Twist();
    while not rospy.is_shutdown():
	msg.linear.x=5;
	msg.linear.y=0.0;
	msg.linear.z=0.0;
	msg.angular.x=5;
	msg.angular.y=0.0;
	msg.angular.z=0.0;
	pub.publish(msg);
        
        rate.sleep()    # 500msec

if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass

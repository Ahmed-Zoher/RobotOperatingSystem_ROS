#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
current_pos=0;
prev_pos=0;

def functionCb(msg):
    global current_pos
    global prev_pos
    current_pos=float(msg.linear.x);
    velocity = float((float(current_pos)-float(prev_pos))*0.5);
    if (float(velocity) == 0):
	print("Robot Stopped");
    else:
	print("Robot is moving Forward with velocity: " + str(velocity));
    prev_pos=float(current_pos);

def subscriber():
    rospy.init_node('node_3', anonymous=True)
    rospy.Subscriber('/motor/vel_msg', Twist, functionCb)
  

    rospy.spin()

if __name__== '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass

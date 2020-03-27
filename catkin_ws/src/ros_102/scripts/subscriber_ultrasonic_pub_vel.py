#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
obstacle=0;

def functionCb(msg):
    global obstacle
    #rospy.loginfo("Received msg from /sensor/ultrasonic is: %s", msg.data)
    obstacle=msg.data;



def subscriber():
    rospy.init_node('node_2', anonymous=True)
    rospy.Subscriber('/sensor/ultrasonic', String, functionCb)

    pub = rospy.Publisher('/motor/vel_msg', Twist, queue_size=7)
    rate = rospy.Rate(0.5) # 2secs
    msg1=Twist();

    velocity=0;
    velocity_inc=0.1428571429;
    velocity_dec=0.125;
    position=0;
    while not rospy.is_shutdown():
        if (int(obstacle) < 30):
		velocity=0;
	if (30 <= int(obstacle) < 70):
		velocity=velocity-velocity_dec;	
	if (70 <= int(obstacle) < 101):
		velocity=velocity+velocity_inc;	

	position=position+(velocity*2);
	msg1.linear.x=position; # velocity=distance/time
	msg1.linear.y=0.0;
	msg1.linear.z=0.0;
	msg1.angular.x=0;
	msg1.angular.y=0.0;
	msg1.angular.z=0.0;
	pub.publish(msg1);
        
        rate.sleep()    # 500msec

    rospy.spin()


if __name__== '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass







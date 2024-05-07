#!/usr/bin/env python
import rospy 
from ackermann_msgs.msg import AckermannDriveStamped

def talker():
    v=rospy.get_param("~v",0.0)
    d=rospy.get_param("~d",0.0)
    
    pub=rospy.Publisher('drive',AckermannDriveStamped,queue_size=10)

    msg=AckermannDriveStamped()
    msg.drive.speed=v
    msg.drive.steering_angle=d

    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

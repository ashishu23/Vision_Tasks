#!/usr/bin/env python3

import rospy 
from ackermann_msgs.msg import AckermannDriveStamped

def callback(msg):
    new_speed=msg.drive.speed*3
    new_steering_angle=msg.drive.steering_angle*3

    new_msg=AckermannDriveStamped()
    new_msg.drive.speed=new_speed
    new_msg.drive.steering_angle=new_steering_angle

    drive_relay_pub.publish(new_msg)

def relay():
    rospy.init_node('relay',anonymous=True)

    rospy.Subscriber('drive',AckermannDriveStamped,callback)

    global drive_relay_pub
    drive_relay_pub=rospy.Publisher('drive_relay',AckermannDriveStamped,queue_size=10)
    rospy.spin()

if __name__=='__main__':
    try:
        relay()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/python 
import rospy 
from std_msgs.msg import String
from car import RemoteCar
from time import sleep

def callback(data,dc):
    commd  = data.data
    rospy.loginfo(commd)
    for cmd in commd:
        #print cmd 
        if cmd =='w':
            print 'forward'
            dc.drive(1)
        elif cmd =='s':
            dc.drive(-1) 
        elif cmd =='a':
            dc.turn(-1)
        elif cmd =='d':
            dc.turn(1)
        elif cmd =='q':
            print 'stop'
            dc.stop()
        sleep(2)
        #dc.stop()

def drive_listener():
    # init node 
    rospy.init_node("drive_listener",anonymous=True)
    dc = RemoteCar()
    rospy.Subscriber("rc_command",String, callback, dc)
    rospy.spin()

if __name__ == "__main__":
    print("running car drive scripts")
    drive_listener()

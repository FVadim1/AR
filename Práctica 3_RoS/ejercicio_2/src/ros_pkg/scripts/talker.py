#!/usr/bin/env python3
# license removed for brevity
import rospy
import random
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('topico_medidas', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz

    arriba = 0
    abajo = 1
    izquierda = 2
    derecha = 3
    while not rospy.is_shutdown():
        x = random.randint(0, 1)

        if x == 1:
            msg = '{"arriba":'+str(arriba)+',"abajo":'+str(abajo)+',"izquierda":'+str(izquierda)+',"derecha":'+str(derecha)+'}'       
        else:
            msg = "-1" #GIRANDO
        
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

        arriba += 1
        abajo += 1
        izquierda += 1
        derecha += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException as msg:
        print(msg)




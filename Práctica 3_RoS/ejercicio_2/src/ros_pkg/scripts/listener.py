#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

i = 0

def callback(data):
    global i
    if i % 4 == 0: #cada 4
        if data.data == "-1":
            rospy.loginfo("GIRO")
            rospy.loginfo("\n")
        else:
            data = eval(data.data)
            largo = data["arriba"] + data["abajo"]
            ancho = data["izquierda"] + data["derecha"]
            superficie = largo*ancho
            x = data["izquierda"] 
            y = data["abajo"]
            rospy.loginfo(f"El largo de la habitación es {largo}")
            rospy.loginfo(f"El ancho de la habitación es {ancho}")
            rospy.loginfo(f"La superficie de la habitación es {superficie}")
            rospy.loginfo(f"La posición del robot en coordenadas es X={x} , Y={y}")
            rospy.loginfo("\n")
    i=i+1  
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("topico_medidas", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()



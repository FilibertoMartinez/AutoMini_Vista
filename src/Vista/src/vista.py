#!/usr/bin/python

import rospy
import cv2
import numpy as np

from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage, Image

def nothing(x):
    """Hacer nada"""
    pass

def redimensionImagen(frame,escala):
    ancho = int(frame.shape[1] * escala / 100)
    largo = int(frame.shape[0] * escala / 100)
    nuevaDimension = (ancho,largo)
    frameResize = cv2.resize(frame, nuevaDimension, interpolation = cv2.INTER_AREA)
    return frameResize

class Nodo(object):
    def __init__(self):
        # Params
        self.br = CvBridge()            #Se crea el puente para uso de OpenCV
        self.recorte = None
        # Node cycle rate (in Hz).
        self.loop_rate = rospy.Rate(30)
	
	# Publishers
        self.pub = rospy.Publisher('imageROI_CUT', Image,queue_size=10)
        # Subscribers
        rospy.Subscriber("/app/camera/rgb/image_raw/compressed",CompressedImage,self.callback)

    def callback(self, msg):
        np_arr = np.fromstring(msg.data, np.uint8)  
        self.cv_frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR) 

        escala = 100 # En porcentaje
        cv_frame=redimensionImagen(self.cv_frame,escala)
        
        self.recorte=cv_frame[225:410,0:640]
        cv2.imshow("Vista",self.recorte)                      #Se muestra en una ventana la Imagen capturada
    
        cv2.waitKey(1)                                              #Mantiene las ventanas en pantalla

    def start(self):
        rospy.loginfo("Timing images")
        #rospy.spin()
        while not rospy.is_shutdown():
            rospy.loginfo('publishing image')
            if self.recorte is not None:
                self.pub.publish(self.br.cv2_to_imgmsg(self.recorte))
            self.loop_rate.sleep()

if __name__ == '__main__':
    rospy.init_node("VISTA", anonymous=True)
    my_node = Nodo()
    my_node.start()

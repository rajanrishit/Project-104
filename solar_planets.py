import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (105,100),
            cv2.FONT_HERSHEY_COMPLEX,
            1.5,
            (25,255,255)
            )

cv2.putText(img,
            "Mercury",
            (120,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (25,255,25)
            )     

cv2.putText(img,
            "Venus",
            (190,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (25,25,255)
            )            

cv2.putText(img,
            "Earth",
            (290,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (25,255,255)
            )

cv2.putText(img,
            "Mars",
            (385,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (25,255,55)
            )

cv2.putText(img,
            "Jupitar",
            (510,380),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (25,200,255)
            )    

cv2.putText(img,
            "Saturn",
            (770,320),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (25,255,25)
            )   

cv2.putText(img,
            "Uranus",
            (965,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )    

cv2.putText(img,
            "Neptune",
            (1110,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (25,25,255)
            )                                     

cv2.imshow("Output",img)
cv2.imwrite("Solar_systemwithRishit.jpg",img)
cv2.waitKey(0)

# Code used by user on their personal devices IDE(pyhton)
# pip install
import cv2
import  urllib.request
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(maxHands=1 , detectionCon=0.8 )

cap = cv2.VideoCapture(1)

while True:
    ret,  photo = cap.read()
    hand = detector.findHands(photo , draw=False)
    if hand:
        detectHand = hand[0]
        if detectHand:
            fingerup = detector.fingersUp(detectHand)
            if detectHand['type'] == 'Left':
                for i in fingerup:
                    if i==1:
                        urllib.request.urlopen('https://3ce8icjupoi.execute-api.ap-south-1.amazonaws.com/test/docker')
            else:
                for i in fingerup:
                    if i==1:
                        urllib.request.urlopen('https://3ce8icjupoi.execute-api.ap-south-1.amazonaws.com/test/deletecon')
            
    cv2.imshow("my photo", photo)
    if cv2.waitKey(1) == 10:
        break
        
cv2.destroyAllWindows()
cap.release()
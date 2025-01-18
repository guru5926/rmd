import cv2
from cvzone.HandTrackingModule import HandDetector
import controller as cnt  # Make sure controller.py is in the same directory

# Initialize the hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Start capturing video
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Define a dictionary to map finger count to text
finger_count_text = {
    (0,0,0,0,0): 'Finger count:0',
    (0,1,0,0,0): 'Finger count:1',
    (0,1,1,0,0): 'Finger count:2',
    (0,1,1,1,0): 'Finger count:3',
    (0,1,1,1,1): 'Finger count:4',
    (1,1,1,1,1): 'Finger count:5'
}

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)
    
    if hands:
        lmList = hands[0]
        fingerUp = tuple(detector.fingersUp(lmList))  # Convert list to tuple
        print(fingerUp)
        cnt.led(fingerUp)
        
        # Get the corresponding text from the dictionary
        text = finger_count_text.get(fingerUp, 'Unknown gesture')
        cv2.putText(frame, text, (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
    
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()

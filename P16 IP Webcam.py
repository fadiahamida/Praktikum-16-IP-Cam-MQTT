import cv2
cap = cv2.VideoCapture("http://10.223.20.137:8080/video")
while True:
    ret, frame = cap.read()
    cv2.imshow('IP Cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
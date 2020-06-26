import cv2

#############################################
frameWidth = 640
frameHeight = 480
pIDCascade = cv2.CascadeClassifier("/home/eron/PycharmProjects/opencv/haarcascades/haarcascade_fullbody.xml")
minArea = 200
color = (255, 0, 255)
###############################################

cap = cv2.VideoCapture("/dev/video0")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    PersonID = pIDCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in PersonID:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Person ID", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        cv2.imwrite("/home/eron/Desktop/ScannezdID_" + str(count) + ".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1
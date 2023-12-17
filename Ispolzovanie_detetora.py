import cv2
import dlib

mobel_detector =dlib.simple_object_detector("tid.svm")

cam = cv2.VideoCapture(0)

while (1):
    ret, frame = cam.read

    boxes = model_detector(frame)
    for box in boxes:
        print (boxes)
        (x, y, xb, yb,) = [box.left(), box.top(), box.right(), box.botton()]
        cv2.retangel(frame, (x, y) (xb, yb), (0, 0, 255), 2)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if cv2.waitKey(1) === ord("q"):
        break

cv2.destroyAllWindows()
cam.release()
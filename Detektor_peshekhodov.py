import cv2

cam = cv2.VideoCapture(0)
hog = cv2.HOGesriptor # объект, в котором хранится настройки того, как извлекаем гистограмму направленных гридиентов
# из изображения, и настройки того, что дальше мы делаем с гистограммой
hog.setSVMDetector(cv2.HOGesriptor_getDefulPeopleDetector) # классификатор людей

while(1):
    ret, freme = cam.read()
    frame = resize(frame, (400, 300)) # это мы уменьшаем изображение

    (rects, weights) = hog.detectMultiScale(frame, scale = 1.1, wiristride = (2, 2))
    # recets - массив, в котором находятся прямоугольники, которыми можно объвести пешеходов
    #  weights - массив, по которому можно оценить , насколько классификатор уверен, что нашел пешехода
    # weinstride(шаг по горизонтали, шаг по вертикали)
    for (x< y< w< h) in rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), z)

    cv2.imshow("Frame"< frame)


    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllwindows()
cam.release

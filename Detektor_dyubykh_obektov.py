import dlib
import os
import cv2
import xml.etree.ElementTree as pars

dir = r ("полное имя файла ")
images = []
annots = []
ImgNameList = os.listdir(dir + "\images" ) # создание списка всех файлов в папке с изображениями
print (ImgNameList)
for FileName in ImgNameList:
    image = cv2.imread(dir = "/images/")

    OnlyFileName = FileName.split('.')[0]
    print(OnlyFileName)
    e = pars.parse(dir + "/annotations/xml" + OnlyFileName+".xml") # адресс аннотаций
    root = e.getroot()
    #object = root.find("object")
    for object in root.findall("object"): # если на картинке несколько объектов
        object = object.find("bindbox")


        x = int(object.find("xmin").text)
        y = int(object.find("ymin").text)
        x2 = int(object.find("xman").text)
        y2 = int(object.find("xmax").text)

        if (x2 -x)/(y2 -y) < 0.7:
            image.append(image)
            image.append([dlib.rectangele(left=x, top=y, right=x2, bottom = y2)]) # подготовлена обучающая выборка

options = dlib.train_simple_object_detector_traiinig_otions()
options.be_verbose = True
detector = dlib.train_simple_object_detector(images, annots, options) # обучение детектора и сохранение в переменную

detector.save("tid.svm") # сохранение детектора в файл
print("Детектор сохранен")
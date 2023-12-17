import cv2 as cv
import random
import numpy as np

cap = cv.imread("1.jpg")

one_top = cv.imread("1_1.jpg")
one_bottom = cv.imread("1_4.jpg")
one_right = cv.imread("1_3.jpg")
one_left = cv.imread("1_2.jpg")
two_top = cv.imread("2_2.jpg")
two_bottom = cv.imread("2_4.jpg")
two_right = cv.imread("2_1.jpg")
two_left = cv.imread("2_3.jpg")
three_top = cv.imread("3_1.jpg")
three_left = cv.imread("3_2.jpg")
three_right = cv.imread("3_4.jpg")
three_bottom = cv.imread("3_3.jpg")

one_left = cv.resize(one_left, (50, 30))
one_right = cv.resize(one_right, (50, 30))
one_top = cv.resize(one_top, (30, 50))
one_bottom = cv.resize(one_bottom, (30, 50))
two_left = cv.resize(two_left, (50, 30))
two_right = cv.resize(two_right, (50, 30))
two_bottom = cv.resize(two_bottom, (30, 50))
two_top = cv.resize(two_top, (30, 50))
three_left = cv.resize(three_left, (50, 30))
three_right = cv.resize(three_right, (50, 30))
three_top = cv.resize(three_top, (30, 50))
three_bottom = cv.resize(three_bottom, (30, 50))

one_left = cv.inRange(cv.cvtColor(one_left, cv.COLOR_BGR2GRAY), 200, 255)
one_right = cv.inRange(cv.cvtColor(one_right, cv.COLOR_BGR2GRAY), 200, 255)
one_top = cv.inRange(cv.cvtColor(one_top, cv.COLOR_BGR2GRAY), 200, 255)
one_bottom = cv.inRange(cv.cvtColor(one_bottom, cv.COLOR_BGR2GRAY), 210, 255)
two_top = cv.inRange(cv.cvtColor(two_top, cv.COLOR_BGR2GRAY), 200, 255)
two_bottom = cv.inRange(cv.cvtColor(two_bottom, cv.COLOR_BGR2GRAY), 210, 255)
two_left = cv.inRange(cv.cvtColor(two_left, cv.COLOR_BGR2GRAY), 200, 255)
two_right = cv.inRange(cv.cvtColor(two_right, cv.COLOR_BGR2GRAY), 200, 255)
three_top = cv.inRange(cv.cvtColor(three_top, cv.COLOR_BGR2GRAY), 200, 255)
three_bottom = cv.inRange(cv.cvtColor(three_bottom, cv.COLOR_BGR2GRAY), 200, 255)
three_left = cv.inRange(cv.cvtColor(three_left, cv.COLOR_BGR2GRAY), 200, 255)
three_right = cv.inRange(cv.cvtColor(three_right, cv.COLOR_BGR2GRAY), 200, 255)

fn = 'example.jpg'  # имя файла, который будем анализировать
img = cv.imread(fn)
img = img[250:, :]
print(1)
vec = []
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thresh = cv.inRange(gray, 200, 255)# применяем цветовой фильтр
contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.imshow('filter', thresh)
    # перебираем все найденные контуры в цикле
for cnt in contours0:
    rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
    box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
    box = np.int0(box)  # округление координат
    dx = abs(box[1][0] - box[0][0])
    dy = abs(box[0][1] - box[1][1])
    print(dx, dy)
    if (dx < dy and dx < 18 and dy < 60 and dx > -1 and dy >= 27) or (dy < dx and dx < 60 and dy < 24 and dx > 27 and dy > -1) and abs(dx - dy) > 20:
        x, xm = max([box[1][0], box[0][0], box[2][0], box[3][0]]), min([box[1][0], box[0][0], box[2][0], box[3][0]])# рисуем прямоугольник
        y, ym = max([box[1][1], box[0][1], box[2][1], box[3][1]]), min([box[1][1], box[0][1], box[2][1], box[3][1]])
        digit = thresh[ym:y, xm:x]
        print(dx, dy)
        if y - ym > x - xm:
            digit = cv.resize(digit, (30, 50))
            cv.imshow("89", digit)
            cv.drawContours(img, [box], -1, (255, 0, 0), 0)
            nabor = [0, 0, 0, 0, 0, 0]
        
            for i in range(50):
                for j in range(30):
                    if digit[i][j] == one_top[i][j]:
                        nabor[0] += 1
                    if digit[i][j] == one_bottom[i][j]:
                        nabor[1] += 1
                    if digit[i][j] == two_top[i][j]:
                        nabor[2] += 1
                    if digit[i][j] == two_bottom[i][j]:
                        nabor[3] += 1
                    if digit[i][j] == three_top[i][j]:
                        nabor[4] += 1
                    if digit[i][j] == three_bottom[i][j]:
                        nabor[5] += 1
                        
            vec.append([nabor.index(max(nabor)) // 2 + 1, x])

        else:
            digit = cv.resize(digit, (50, 30))
            cv.drawContours(img, [box], -1, (255, 0, 0), 0)
            
            nabor = [0, 0, 0, 0, 0, 0]
       

        
            for i in range(30):
                for j in range(50):
                    if digit[i][j] == one_left[i][j]:
                        nabor[0] += 1
                    if digit[i][j] == one_right[i][j]:
                        nabor[1] += 1
                    if digit[i][j] == two_left[i][j]:
                        nabor[2] += 1
                    if digit[i][j] == two_right[i][j]:
                        nabor[3] += 1
                    if digit[i][j] == three_left[i][j]:
                        nabor[4] += 1
                    if digit[i][j] == three_right[i][j]:
                        nabor[5] += 1

            vec.append([nabor.index(max(nabor)) // 2 + 1, x])
        

print(sorted(vec, key=lambda x: x[1]))           
cv.imshow('contours', img)  # вывод обработанного кадра в окно

cv.waitKey()
cv.destroyAllWindows()




















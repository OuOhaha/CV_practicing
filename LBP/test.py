#Written by OuOhaha
import cv2 as cv
import numpy as np

#可調整的參數設定
RESIZE_MULTIPLIER = 1 #影像縮放倍率

#讀取影像並轉灰階存入img變數 & 調整縮放至指定倍率
img = cv.imread('picture\\test.jpg', cv.IMREAD_GRAYSCALE) 
img = cv.resize(img, (int(img.shape[1] * RESIZE_MULTIPLIER), int(img.shape[0] * RESIZE_MULTIPLIER)))
img_rows, img_columns = img.shape
print('Current resolution :', img_columns, '*', img_rows)

#創建一張空白LBP特徵圖
LBP_map = np.zeros((img_rows, img_columns), dtype = np.uint8)

#LBP的mask(3*3)移動
for i in range (1, img_rows - 1):
    for j in range (1, img_columns - 1):
        mask_center = img[i, j] #mask中間值
        feature_value = 00000000 #比對值初始化(8位元示意)
        
        #特徵比對(左上開始順時針進行) & 以二進制存值
        feature_value |= (img[i - 1, j - 1] > mask_center) << 7
        feature_value |= (img[i - 1, j] > mask_center) << 6
        feature_value |= (img[i - 1, j + 1] > mask_center) << 5
        feature_value |= (img[i, j + 1] > mask_center) << 4
        feature_value |= (img[i + 1, j + 1] > mask_center) << 3
        feature_value |= (img[i + 1, j] > mask_center) << 2
        feature_value |= (img[i + 1, j - 1] > mask_center) << 1
        feature_value |= (img[i, j - 1] > mask_center) << 0
        
        #將值存入特徵圖當中
        LBP_map[i, j] = feature_value

#調整視窗
cv.namedWindow('Original', cv.WINDOW_NORMAL)
cv.namedWindow('LBP', cv.WINDOW_NORMAL)

#顯示原始圖片+LBP特徵圖
cv.imshow('Original', img)
cv.imshow('LBP', LBP_map)
cv.waitKey(0)
cv.destroyAllWindows()
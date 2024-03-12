import cv2
import numpy as np

# 读取原图像来获取高度和宽度
img = cv2.imread(r'E:\seg-master\runs\predict-seg\exp5\0X1E9465782E2D5B16_frame15.jpg')
h, w, _ = img.shape

# 读取txt文件，假设txt文件中每行格式为：class, x1 y1, x2 y2, ..., xn yn
def calculate_area_from_txt(txt_file):
    with open(txt_file, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            cls = int(data[0].split()[0])  # 提取空格前的整数作为类别
            points = [float(val) for val in data[0].split()[1:]]  # 提取空格后的坐标信息

            # 将归一化坐标转换为像素坐标
            pixel_coords = [(int(x * w), int(y * h)) for x, y in zip(points[::2], points[1::2])]

            # 计算多边形的面积
            area = cv2.contourArea(np.array(pixel_coords).reshape((-1, 1, 2)))
            print(f"Class {cls}: Area = {area}")

# 调用函数计算各个类别的面积
calculate_area_from_txt(r'E:\yolov5-seg-master\runs\predict-seg\exp5\labels\0X1E9465782E2D5B16_frame15.txt')
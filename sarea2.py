import cv2
import numpy as np
import os
import csv

# 定义图像目录和txt文件目录
image_dir = r'E:\echonet-master\frames'
txt_dir = r'E:\seg-master\runs\predict-seg\exp6\labels'

# 创建CSV文件并写入表头
with open('area_results.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Filename', 'Class', 'Area'])

# 读取txt文件并计算面积
for txt_file in os.listdir(txt_dir):
    image_name = txt_file.replace('.txt', '.jpg')  # 根据txt文件名获取对应的图片文件名

    # 读取图像来获取高度和宽度
    img = cv2.imread(os.path.join(image_dir, image_name))
    h, w, _ = img.shape

    with open(os.path.join(txt_dir, txt_file), 'r') as f:
        for line in f:
            data = line.strip().split(',')
            cls = int(data[0].split()[0])  # 提取空格前的整数作为类别
            points = [float(val) for val in data[0].split()[1:]]  # 提取空格后的坐标信息

            # 将归一化坐标转换为像素坐标
            pixel_coords = [(int(x * w), int(y * h)) for x, y in zip(points[::2], points[1::2])]

            # 计算多边形的面积
            area = cv2.contourArea(np.array(pixel_coords).reshape((-1, 1, 2)))

            # 写入结果到CSV文件
            with open('area_results.csv', 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([image_name, cls, area])
import pandas as pd
import matplotlib.pyplot as plt

# 从 CSV 文件读取数据
df = pd.read_csv(r'E:\seg-master\path_to_save_csv_file.csv')

# 创建画布和坐标轴
plt.figure(figsize=(8, 6))
plt.title('Connect Points in Order of CSV Rows')
plt.xlabel('X')
plt.ylabel('Y')

# 提取 x 和 y 列的数据
x_values = df['X'].tolist()
y_values = df['Y'].tolist()

# 绘制连续线图
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')

plt.grid(True)
plt.show()
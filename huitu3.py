import pandas as pd
import matplotlib.pyplot as plt

# 从 CSV 文件读取数据
df = pd.read_csv(r'E:\seg-master\path_to_save_csv_file.csv')

# 提取 x 和 y 列的数据
x_values = df['X'].tolist()
y_values = df['Y'].tolist()

# 创建散点图
plt.scatter(x_values, y_values, color='b', marker='o')
plt.title('Scatter Plot of X and Y coordinates')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
data = pd.read_csv(r'E:\seg-master\area_results.csv')

# 获取第三列数据
values = data.iloc[:, 2]

# 绘制曲线图
plt.figure(figsize=(10, 6))
plt.plot(values, color='b', marker='o', linestyle='-')
plt.title('Curve from Third Column')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()
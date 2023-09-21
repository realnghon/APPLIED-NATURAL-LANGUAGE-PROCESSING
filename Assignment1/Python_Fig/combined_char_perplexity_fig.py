import matplotlib.pyplot as plt

# 数据
ngram = [1, 2, 3, 4, 5, 6]
orgin_char_train = [93.81, 27.28, 21.61, 16.20, 12.46, 5.15]
orgin_char_test = [93.68, 27.23, 21.61, 16.21, 12.81, 5.26]
Expansion_char_train = [122.08, 41.03, 26.98, 16.95, 10.87, 3.92]
Expansion_char_test = [120.67, 41.14, 27.18, 17.18, 11.15, 4.13]

# 创建一个新的图形，并设置合适的尺寸
plt.figure(figsize=(8, 5))

# 绘制扩张数据后的折线（虚线）
plt.plot(ngram, Expansion_char_train, marker='s', linestyle='--', label='Expanded dataset - Train')
plt.plot(ngram, Expansion_char_test, marker='s', linestyle='--', label='Expanded dataset - Test')

# 绘制未扩张数据的折线（实线）
plt.plot(ngram, orgin_char_train, marker='o', linestyle='-', label='Origin dataset - Train')
plt.plot(ngram, orgin_char_test, marker='o', linestyle='-', label='Origin dataset - Test')

# 添加标题和标签
plt.xlabel('n-gram')
plt.ylabel('perplexity')

# 设置横轴刻度为整数
plt.xticks(ngram)

# 添加图例
plt.legend()

# 显示网格
plt.grid(True, linestyle='--', alpha=0.6)

# 调整字体大小
plt.rc('font', size=12)

# 保存图像
plt.savefig('combined_char_perplexity.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()

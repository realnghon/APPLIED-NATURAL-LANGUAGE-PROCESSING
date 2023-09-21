import matplotlib.pyplot as plt

# 数据
ngram = [1, 2, 3]
orgin_word_train = [471.87, 175.10, 82.12]
orgin_word_test = [450.52, 227.95, 195.17]
Expansion_word_train = [674.56, 264.58, 132.54]
Expansion_word_test = [634.34, 303.63, 252.48]
orgin_char_train = [2372.35, 150.67, 106.73]
orgin_char_test = [1960.92, 379.16, 320.65]
Expansion_char_train = [471.87, 175.10, 82.12]
Expansion_char_test = [450.52, 227.95, 195.17]

# 创建一个新的图形，并设置合适的尺寸
plt.figure(figsize=(8, 5))

# 绘制扩张数据后的折线（虚线）
plt.plot(ngram, Expansion_word_train, marker='s', linestyle='--', label='Expanded dataset - Train')
plt.plot(ngram, Expansion_word_test, marker='s', linestyle='--', label='Expanded dataset - Test')

# 绘制未扩张数据的折线（实线）
plt.plot(ngram, orgin_word_train, marker='o', linestyle='-', label='Origin dataset - Train')
plt.plot(ngram, orgin_word_test, marker='o', linestyle='-', label='Origin dataset - Test')

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
plt.savefig('combined_word_perplexity.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()

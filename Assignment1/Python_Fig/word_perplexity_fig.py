import matplotlib.pyplot as plt

# 数据
ngram = [1, 2, 3]
train_no_prep_smo = [2372.35, 150.67, 106.73]
test_no_prep_smo = [1960.92, 379.16, 320.65]
train_prep_smo = [471.87, 175.10, 82.12]
test_prep_smo = [450.52, 227.95, 195.17]

# 创建一个新的图形，并设置合适的尺寸
plt.figure(figsize=(8, 5))

# 绘制训练数据的折线（虚线）
plt.plot(ngram, train_no_prep_smo, marker='o', linestyle='--', label='Train (No Prep & Smo)')
plt.plot(ngram, train_prep_smo, marker='o', linestyle='--', label='Train (Prep & Smo)')

# 绘制测试数据的折线（实线）
plt.plot(ngram, test_no_prep_smo, marker='o', linestyle='-', label='Test (No Prep & Smo)')
plt.plot(ngram, test_prep_smo, marker='o', linestyle='-', label='Test (Prep & Smo)')

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
plt.savefig('word_perplexity.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()

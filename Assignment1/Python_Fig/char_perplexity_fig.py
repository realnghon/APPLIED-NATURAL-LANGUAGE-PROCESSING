import matplotlib.pyplot as plt

# 数据
ngram = [1, 2, 3, 4, 5, 6]

train_prep_smo = [93.81, 27.28, 21.61, 16.20, 12.46, 5.15]
test_prep_smo = [93.68, 27.23, 21.61, 16.21, 12.81, 5.26]

# 创建一个新的图形，并设置合适的尺寸
plt.figure(figsize=(8, 5))

plt.plot(ngram, train_prep_smo, marker='o', markersize=8, linestyle='--', label='Train (Prep & Smo)', linewidth=2,
         color='blue')
plt.plot(ngram, test_prep_smo, marker='s', markersize=8, linestyle=':', label='Test (Prep & Smo)', linewidth=2,
         color='green')
# 添加文字描述到图例
plt.legend(['Train (Prep & Smo)', 'Test (Prep & Smo)'])

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
plt.savefig('char_perplexity.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()

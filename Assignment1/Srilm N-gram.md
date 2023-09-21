# Srilm N-gram

### Srilm 编译

export SRILM=/home/nghon/srilm
export PATH=$PATH:$SRILM/bin:$SRILM/bin/i686-m64

sudo apt install make

sudo apt update  # 更新包列表
sudo apt install gcc  # 安装 GCC

sudo apt update  # 更新包列表
sudo apt install g++

make

### 数据准备

数据合并

```bash
cat data/news.train data/news.2007.en.shuffled > data/combined.train
```

文本清洗 - 全部小写，去除标点符号

stopwords - [All English Stopwords (700+) | Kaggle](https://www.kaggle.com/datasets/rowhitswami/stopwords)

```bash
awk 'BEGIN{IGNORECASE=1} NR==FNR{stopwords[tolower($0)]; next} {gsub(/[[:punct:]]/, ""); for (i=1; i<=NF; i++) {word=tolower($i); if (!(word in stopwords)) printf word" "} print ""}' data/stopwords.txt data/news.train > data/processed_news.train
```

文本分割

```bash
perl -C -lne 'print join(" ", split(""))' data/combined.train > data/combined.train.split
```

### **Word-Based**

无数据预处理

```bash
bin/i686-m64/ngram-count -order 3 -text data/news.train -lm data/models/news_word.lm

bin/i686-m64/ngram -lm data/models/news_word.lm -order 1 -ppl data/news.train
bin/i686-m64/ngram -lm data/models/news_word.lm -order 1 -ppl data/news.test
bin/i686-m64/ngram -lm data/models/news_word.lm -order 2 -ppl data/news.train
bin/i686-m64/ngram -lm data/models/news_word.lm -order 2 -ppl data/news.test
bin/i686-m64/ngram -lm data/models/news_word.lm -order 3 -ppl data/news.train
bin/i686-m64/ngram -lm data/models/news_word.lm -order 3 -ppl data/news.test
```

![Untitled](Srilm%20N-gram%20aad686f95c6d47e6b00f2d29f5a4dd67/Untitled.png)

数据预处理加平滑

```bash
awk 'BEGIN{IGNORECASE=1} NR==FNR{stopwords[tolower($0)]; next} {gsub(/[[:punct:]]/, ""); for (i=1; i<=NF; i++) {word=tolower($i); if (!(word in stopwords)) printf word" "} print ""}' data/stopwords.txt data/news.train > data/processed_news.train
```

```bash
bin/i686-m64/ngram-count -text data/processed_news.train -order 3 -lm data/models/tuned_news_word.lm -kndiscount -interpolate -gt3min 1 -gt4min 1 -gt5min 1 -gt6min 1 -unk -map-unk "<unk>"

bin/i686-m64/ngram -lm data/models/tuned_news_word.lm -order 1 -ppl data/news.train
bin/i686-m64/ngram -lm data/models/tuned_news_word.lm -order 1 -ppl data/news.test
bin/i686-m64/ngram -lm data/models/tuned_news_word.lm -order 2 -ppl data/news.train
bin/i686-m64/ngram -lm data/models/tuned_news_word.lm -order 2 -ppl data/news.test
bin/i686-m64/ngram -lm data/models/tuned_news_word.lm -order 3 -ppl data/news.train
bin/i686-m64/ngram -lm data/models/tuned_news_word.lm -order 3 -ppl data/news.test
```

![Untitled](Srilm%20N-gram%20aad686f95c6d47e6b00f2d29f5a4dd67/Untitled%201.png)

### Character-Based

数据预处理加平滑

```bash
perl -C -lne 'print join(" ", split(""))' data/processed_news.train > data/processed_news.train.split
perl -C -lne 'print join(" ", split(""))' data/news.train > data/news.train.split
perl -C -lne 'print join(" ", split(""))' data/news.test > data/news.test.split
```

```bash
bin/i686-m64/ngram-count -text data/processed_news.train.split -order 6 -lm data/models/tuned_news_char.lm -kndiscount
```

```bash
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 1 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 1 -ppl data/news.test.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 2 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 2 -ppl data/news.test.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 3 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 3 -ppl data/news.test.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 4 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 4 -ppl data/news.test.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 5 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 5 -ppl data/news.test.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 6 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_news_char.lm -order 6 -ppl data/news.test.split
```

![Untitled](Srilm%20N-gram%20aad686f95c6d47e6b00f2d29f5a4dd67/Untitled%202.png)

### Combined-Word-Based

```bash
cat data/news.train data/news.2007.en.shuffled > data/combined.train
```

```bash
awk 'BEGIN{IGNORECASE=1} NR==FNR{stopwords[tolower($0)]; next} {gsub(/[[:punct:]]/, ""); for (i=1; i<=NF; i++) {word=tolower($i); if (!(word in stopwords)) printf word" "} print ""}' data/stopwords.txt data/combined.train > data/processed_combined.train
```

```bash
bin/i686-m64/ngram-count -text data/processed_combined.train -order 3 -lm data/models/tuned_combined_word.lm -kndiscount -interpolate -gt3min 1 -gt4min 1 -gt5min 1 -gt6min 1 -unk -map-unk "<unk>"

bin/i686-m64/ngram -lm data/models/tuned_combined_word.lm -order 1 -ppl data/news.train
bin/i686-m64/ngram -lm data/models/tuned_combined_word.lm -order 1 -ppl data/news.test
bin/i686-m64/ngram -lm data/models/tuned_combined_word.lm -order 2 -ppl data/news.train
bin/i686-m64/ngram -lm data/models/tuned_combined_word.lm -order 2 -ppl data/news.test
bin/i686-m64/ngram -lm data/models/tuned_combined_word.lm -order 3 -ppl data/news.train
bin/i686-m64/ngram -lm data/models/tuned_combined_word.lm -order 3 -ppl data/news.test
```

![Untitled](Srilm%20N-gram%20aad686f95c6d47e6b00f2d29f5a4dd67/Untitled%203.png)

### Combined-Character-Based

```bash
perl -C -lne 'print join(" ", split(""))' data/combined.train > data/combined.train.split
```

```bash
bin/i686-m64/ngram-count -text data/combined.train.split -order 6 -lm data/models/tuned_combined_char.lm -kndiscount -interpolate -gt3min 1 -gt4min 1 -gt5min 1 -gt6min 1 -unk -map-unk "<unk>"
```

```bash
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 1 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 1 -ppl data/news.test.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 2 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 2 -ppl data/news.test.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 3 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 3 -ppl data/news.test.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 4 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 4 -ppl data/news.test.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 5 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 5 -ppl data/news.test.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 6 -ppl data/news.train.split
bin/i686-m64/ngram -lm data/models/tuned_combined_char.lm -order 6 -ppl data/news.test.split
```

![Untitled](Srilm%20N-gram%20aad686f95c6d47e6b00f2d29f5a4dd67/Untitled%204.png)
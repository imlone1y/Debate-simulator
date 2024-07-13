# 辯論模擬器

本項目使用兩個語言模型對同一個題目進行辯論，兩個模型分別代表了正方與反方，會相互讀取對方的證詞後做出反擊，以達到辯論的效果。

第三個模型代表裁判，會讀取正方與反方的論詞後個別做出評分。

本項目核心概念為模擬生成式 [對抗神經網路(Generative Adversarial Network)](https://zh.wikipedia.org/zh-tw/%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C)，但模型本身不會因為分數而微調，因此只能作為原理模擬。

## 運行指南

本項目基於 Python 程式語言，使用到外部程式庫 openai。建議使用 [Anaconda](https://www.anaconda.com) 配置 Python 環境。以下設定程序已在 Windows 11 系統上測試通過。以下為控制台/終端機（Console/Terminal/Shell）指令。

### 環境配置

```bash
# 建立 conda 環境，將其命名為 debate，Python 版本 3.11.5
conda create -n debate python=3.11.5
conda activate debate
```


```bash
# 安?外部程式庫
pip install -r requirements.txt
```

### 運行測試

本項目需要用到 OpenAI API keys，需於 [OpenAI 官網](https://platform.openai.com/api-keys)申請個人的 API keys (須付費)，並將生成的 keys 複製至 `api_keys.py`。

環境配置完成後，可以在 `debate/` 資料夾底下運行 `main.py`。

```bash
cd [項目上方資料夾]/debate
python main.py
```

### 查看辯論紀錄

項目會自動生成文字檔於項目資料夾中，打開即可查看辯論紀錄及裁判評分結果。
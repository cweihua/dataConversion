# dataConversion:将华驼的数据集和鼻咽癌excel病历转换成chatGLM的数据集

本项目将华驼https://github.com/SCIR-HI/Med-ChatGLM 中的train.txt数据集和鼻咽癌病历的excel文件转换成chatGLM微调所需的train.json和dev.json两个文件

## A Quick Start

首先安装依赖包，python环境建议3.9+

```
pip install -r requirements.txt
```

安装完环境后将下载的华驼的数据集train.txt和鼻咽癌的病历 鼻咽癌病历.xlsx 放在桌面上。先将train.txt转换成chatGLM的数据集的格式，得到train2.txt.

```
python MedtochatGLM.py
```

再将 鼻咽癌病历.xlsx 转换成chatGLM的数据集的格式，得到 鼻咽癌训练集.txt，并将它的内容添加到train2.txt中。

```
python exceltochatGLM.py
```

然后将train2.txt转换成json格式得到train2.json

```
python txttojson.py
```

最后将train2.json按7：3的比例随机分割成train.json和dev.json两个文件。

```
python dividejson.py
```

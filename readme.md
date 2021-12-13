# 时光网电影信息爬虫

用于从时光网 (mtime.com) 上爬到海量电影信息，包括导演、演员、年份、影评等。

基于 Python3，依赖 requests、re、bs4。

## 使用方法

`python filmspider.py` 爬取时光网海量电影信息页 url，存储在本地文本文件。

`python filminfospider.py` 根据上一步爬到的 url，爬取各影片和演员的详细信息，json 序列化后存储在本地文本文件。
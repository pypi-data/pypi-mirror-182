# cow_download

## 下载
```
pip install cow_download -i https://pypi.douban.com/simple/
```
## 使用
一个完整的奶牛快传链接就像这样：https://xiyoucloud.cowtransfer.com/s/9f9b7c098b9049  
你可以根据文件的 id 来下载文件 9f9b7c098b9049。

```
cow download 9f9b7c098b9049
```

默认情况下会开启 20 个线程对文件进行下载，这会大大加快下载速度，不过下载速度还受到网络带宽的限制，即下载速度最快不会超过网络带宽。

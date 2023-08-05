# dtools
dtools 爬虫的一些工具库

## 安装
### Required
pip install requests selenium

### 安装 download_tools
```
pip install download_tools
```

## 使用
### 下载文件
download_url()默认使用，也可以设置使用无头selenium，需要浏览器firefox和Firefox驱动

```
import download_tools as dt

page_souce = '<p>测试</p>' dt.download_str(page_souce, r'F:\test', name='测试', suffix='html')

dt.download_url('https://www.baidu.com', r'F:\test') 
```

### headers
```
import download_tools as dt
dt.Headers().get()
dt.Headers(os='win', browser="chrome", headers=True).get()

for i in range(10):
    print(dt.Headers().get())
```
dtools.fake_headers fork from https://pypi.org/project/fake-headers/          
修改：   
* generate()函数名修改为get()


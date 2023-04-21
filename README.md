## FLASK 脚手架

### 背景
- 基于flask，开发脚手架，便于后面项目快速开发(nginx+uwsgi+flask)

### 技术栈
- python3.6以上
- virtualenv 虚拟环境
- 持久化: mysql
- swagger：restx

### swagger 地址
```
http://192.168.100.113:10036/api/v1/
```

### 账户密码

- 账户: admin
- 密码: 123456

### 配置文件

- config/setting.py

### 注意
- 使用了python-dotenv 设置环境变量
- pip install  -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com  -r doc/requirements.txt


## 安装flask_cache 注意点
- 版本号：flask_cache==0.13.1
- No module named ‘werkzeug.contrib‘
  版本兼容性， cd Lib\site-packages\flask_cache ，vim backends.py 
  修改 from cachelib  import (BaseCache, NullCache, SimpleCache, MemcachedCache,  FileSystemCache)
  修改 from werkzeug.contrib.cache import RedisCache 变为 from cachelib import RedisCache
  最后 还是调整为 flask_caching





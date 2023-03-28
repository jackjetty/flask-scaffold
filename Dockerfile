FROM python:3.6.9
MAINTAINER "jeff<jeff@Greathill.com>"
LABEL PROJECT="flask-scaffold" \
      AUTHOR="Jeff"    \
      COMPANY="Greathill Co., Ltd."

RUN ["mkdir","-p","/data/micro-soft/flask-scaffold/"]
RUN ["mkdir","-p","/data/micro-soft/flask-scaffold/logs/"]
WORKDIR /data/micro-soft/flask-scaffold/
# 拷贝当前目录所有的文件，进入 docker 镜像中
COPY . . 
RUN pip install  -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com  -r doc/requirements.txt
# -i https://pypi.tuna.tsinghua.edu.cn/simple 
RUN python -m pip install markupsafe==2.0.1
EXPOSE 10036
ENTRYPOINT  uwsgi --ini uwsgi.ini
#ENTRYPOINT python app.py
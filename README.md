 项目背景介绍,这是一个简单的博客项目,
 在windows10环境下开发
 基于python3.6.5  Django2.0 mysql5.7开发
 计划后续开发为一个前后分离,现在简单的部署使用
 ## 部署环境 ubuntu16.4 python3.5.2 mysql5.7
###  1-使用git clone 项目到服务器

 ```
git clone https://github.com/qiubiteme/DjangoBloger.git
 ```
#####  1.1- 命令行下进入项目目录

 ```
 cd DjangoBloger
 ```
#####  1.2- 查看python版本

 ubuntu下默认安装的是,python2.7,建议安装双版本python,
 pyhton3查看python的版本,具体安装python3的方法google搜索

 ```
 python3
 ```
#####  1.3 安装 virtualenv

 pip3 是安装到python3 的环境中

 ```
 pip3 install virtualenv
 ```
###  2- 创建python3的虚拟环境

 创建 名称为 venv 的虚拟环境

 ```
virtualenv ven
 ```
#####  2.1- 进入虚拟环境虚拟环境

 ```
 source ven/bin/activate
 ```
#####  这是退出虚拟环境命令

 ```
 deactivate
 ```
##### 2.3- 现在可以安装项目依赖

在 DjangoBloger 目录下执行,虚拟环境中

```
pip install -r requirements.txt
```
## 3- 修改配置信息配置

**在项目的DjangoBloger/DjangoBloger目录中创建配置文件,Config.py 添加配置信息**

主要配置是,数据库

```
SECRET_KEY_CONFIG = '这是一段字符串,标识,你的项目唯一性'
# DEBUG 是否开启,生产环境,建议关闭
# CONFIG_DEBUG = False
CONFIG_DEBUG = True
# 服务器配置地址
CONFIG_ALLOWED_HOSTS =['127.0.0.1', 'localhost ', '.qiuyang.date']
# 数据库名字
SQL_NAME = 'bloger'
# 数据库账号
SQL_USER = 'root'
# 服务端mysql密码
# SQL_PASSWORD = ''
# 本地mysql密码
SQL_PASSWORD = ''
# mysql服务器
SQL_HOST = '127.0.0.1'
# 端口
SQL_PORT = '3306'
```
#### 3.1-创建项目需要用的数据库

###### 登录mysql

```
mysql -u root -p
```
###### 创建数据库

 ```
 create database bloger;
 ```
######  查看数据库是否创建成功

```
show databases;
```
#### 3.2-创建数据库表

```
python manage.py makemigrations
```
#### 3.3- 生成数据库表

```
python manage.py migrate
```
**如果默认安装mysql数据库,没有自定义配置,会遇到一个错误,设置方法参阅,配置mysql数据库默认字符集**
```
django.db.utils.InternalError: (1366, "Incorrect string value:
```


## 4- 运行开发服务器,预览效果

```
python manage.py runserver
```
#### 4.1 创建管理员账号并输入两次密码

```
python manage.py createsuperuser
```
### 4.2-提示输入,账号密码

```
Username (leave blank to use 'root'):
Email address:
Password:
Password (again):
Superuser created successfully.
(ven) root@localhost:~/DjangoBloger#
```
### 4.3- 收集项目静态文件

```
python manage.py collectstatic
```

### 4.4- 安装 Gunicorn 服务

```
pip install Gunicorn
```
**运行gunicorn 服务器,预览效果,通过IP 或者域名访问8000 端口**

```
 gunicorn --bind 0.0.0.0:8000 DjangoBloger.wsgi
```
## 5-自动化部署

### 5.1- 创建Gunicorn systemd服务

**在路径 etc/systemd/system下创建gunicorn.service**
添加如下内容
**从该[Unit]部分开始**，该部分用于指定元数据和依赖项。我们将在此处描述我们的服务并告诉init系统仅在达到网络目标后启动它：
接下来，我们将打开该**[Service]部分**。我们将指定要在其下运行的用户,网上很多教程说添加组,问题,这里不添加,
然后，我们将映射工作目录并指定用于启动服务的命令。在这种情况下，我们必须指定Gunicorn可执行文件的完整路径，该文件安装在我们的虚拟环境中。我们将它绑定到项目目录中的Unix套接字，因为Nginx安装在同一台计算机上。这比使用网络端口更安全，更快捷。我们还可以在这里指定任何可选的Gunicorn调整
最后，我们将添加一个**[Install]部分**。如果我们在启动时启动它，这将告诉systemd将此服务链接到什么。我们希望在常规多用户系统启动并运行时启动此服务：

```
[whole]
Description=gunicorn daemon
After=network.target

[Service]
User=root
WorkingDirectory=/home/DjangoBloger
ExecStart=/home/DjangoBloger/ven/bin/gunicorn --workers 3 --bind unix:/home/DjangoBloger/DjangoBloger.sock DjangoBloger.wsgi:application

[Install]
antedBy=multi-user.target
```
systemd服务文件就完成了。立即保存并关闭它

### 5.2- 加载服务

现在可以启动我们创建的Gunicorn服务并启用它以便它在启动时启动

```
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```
### 5.3-检查Gunicorn套接字文件

检查进程的状态以确定它是否能够启动：**没有报错恭喜你,**

```
sudo systemctl status gunicorn
```
如果有错误,仔细检查服务配置,
**可以或查看错误日志**
```
sudo journalctl -u gunicorn
```
## 6-Nginx配置

将Nginx配置为代理传递给Gunicorn

现在Gunicorn已经建立，我们需要配置Nginx以将流量传递给进程。

### 6.1-**在 /etc/nginx  中找到 nginx  conf**

首先在 http 代码块中添加,如下,详细解释如下

**首先指定侦听正常端口80，并且它应该响应我们服务器的域名或IP地址：**

**server_name  后面 有域名写域名,没域名写IP**

 **location = /favicon.ico { access_log off; log_not_found off; }**

**不响应,favicon.ico**

**告诉Nginx在哪里可以找到我们在目录中收集的静态资源。**

**所有这些文件都有一个标准的URI前缀“/ static”，**

**因此我们可以创建一个位置块来匹配这些请求：root /home/DjangoBloger/statict;**

**此路径,根据你自己项目定**

**创建一个`location / {}`块来匹配所有其他请求。在这个位置的内部，我们将包含`proxy_params`Nginx安装中包含的标准文件，然后我们将流量传递给我们的Gunicorn进程创建的套接字** 

**完成后保存并关闭文件** 

```
server {
    listen 80;
    server_name www.qiuyang.date;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/DjangoBloger/statict;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/DjangoBloger/DjangoBloger.sock;
    }
}
```

### 6.2-测试Nginx配置是否存在语法错误：

```
sudo nginx -t
```

如果没有报告错误，请重新启动Nginx： 

### 6.3--重新启动Nginx

```
sudo systemctl restart nginx
```

### 6.4-开启服务器端口

最后，我们需要在端口80上打开正常流量的防火墙。

由于我们不再需要访问开发服务器，我们也可以删除规则以打开端口8000：

##### 开启8000端口

```
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
```

 **如果这两条命令,报 sudo: ufw: command not found  可以需要安装 ufw,然后再执行一遍开启命令**

```
sudo apt-get install ufw
```



 计划分前端和后端模块,基于Django,主要应用有两个,
 Front 和 uadmin 一个前端用户界面,和一个后端管理

windows 使用mysql有个问题
```
在 python2 中，使用 pip install mysql-python 进行安装连接MySQL的库，使用时 import MySQLdb 进行使用

在 python3 中，改变了连接库，改为了 pymysql 库，使用pip install pymysql 进行安装，直接导入即可使用

但是在 Django 中， 连接数据库时使用的是 MySQLdb 库，这在与 python3 的合作中就会报以下错误了

django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'
1
解决方法：在 __init__.py 文件中添加以下代码即可。

import pymysql
pymysql.install_as_MySQLdb()
1
2
额，找了一下却没有找到 install_as_MySQLdb() 这个方法的源码，不过顾名思义应该是让 Django 把 pymysql 当成 MySQLdb 来使用吧
```
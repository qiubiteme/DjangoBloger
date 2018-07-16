 项目背景介绍,这是一个简单的博客项目,
 在windows10环境下开发
 基于python3.6.5  Django2.0 mysql5.7开发
 计划后续开发为一个前后分离,现在简单的部署使用
 ### 部署环境 ubuntu16.4 python3.5.2 mysql5.7
 1-使用git clone 项目到服务器
 ```
git clone https://github.com/qiubiteme/DjangoBloger.git
 ```
 1.1- 命令行下进入项目目录
 ```
 cd DjangoBloger
 ```
 1.2- 查看python版本
 ubuntu下默认安装的是,python2.7,建议安装双版本python,
 pyhton3查看python的版本,具体安装python3的方法google搜索
 ```
 python3
 ```
 1.3 安装 virtualenv
 pip3 是安装到python3 的环境中
 ```
 pip3 install virtualenv
 ```
 2- 创建python3的虚拟环境
 创建 名称为 venv 的虚拟环境
 ```
virtualenv ven
 ```
 2.1- 进入虚拟环境虚拟环境
 ```
 source ven/bin/activate
 ```
2.3- 现在可以安装项目依赖
在 DjangoBloger 目录下执行
```
pip install -r requirements.txt
```
3- 在项目的DjangoBloger/DjangoBloger目录中创建配置文件,Config.py 添加配置信息
主要配置是,数据库
```
SECRET_KEY_CONFIG = '这是一段字符串,标识,你的项目唯一性'
# DEBUG 是否开启,生产环境,建议关闭
# CONFIG_DEBUG = False
CONFIG_DEBUG = True
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
3.1-创建项目需要用的数据库
登录mysql
```
mysql -u root -p
```
创建数据库
 ```
 create database bloger;
 ```
 查看数据库是否创建成功
```
show databases;
```
3.2-创建数据库表
```
python manage.py makemigrations
```
3.3- 生成数据库表
```
python manage.py migrate
```
如果默认安装mysql数据库,没有自定义配置的,会遇到一个
```
django.db.utils.InternalError: (1366, "Incorrect string value:
```
的错误,设置方法参阅,配置mysql数据库默认字符集
4- 运行开发服务器,预览效果
```
python manage.py runserver
```
4.1 创建管理员账号并输入两次密码
```
python manage.py createsuperuser
```
提示输入,账号密码
```
Username (leave blank to use 'root'):
Email address:
Password:
Password (again):
Superuser created successfully.
(ven) root@localhost:~/DjangoBloger#
```
4.2- 安装
```

```
4.3- 收集项目静态文件
```
python manage.py collectstatic
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
 项目背景介绍,这个项目是,一个不可项目
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
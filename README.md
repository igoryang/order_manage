# order_manage
order_manage
搭建环境：python 2.7 + django1.8.14 + mysql_5.6

Django项目：

初始化mysql:   creater database order;   setttings.py  root/123.abc

c:\Python27\python.exe manage.py syncdb  #1.9以上取消此命令

django >1.9以上数据库操作
c:\Python27\python.exe manage.py makemigratios
c:\Python27\python.exe manage.py migrate

c:\Python27\python.exe manage.py runnserver 0.0.0.0 8001

admin-django startproject    -->manage.py startapp  startproject

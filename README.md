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


设置 admin后台 admin.py中设置
--分类管理
--订单管理
--产品管理
list_display 添加显示字段内容
search_fields 添加快速查询栏
list_filter 过滤器
list_per_page 每个表记录分页显示 20/页





设计页面预览：

https://github.com/igoryang/order_manage/blob/master/page_design/front_001.png

https://github.com/igoryang/order_manage/blob/master/page_design/admin_001.png

https://github.com/igoryang/order_manage/blob/master/page_design/admin_type.png

https://github.com/igoryang/order_manage/blob/master/page_design/admin_order.png

https://github.com/igoryang/order_manage/blob/master/page_design/admin_product.png
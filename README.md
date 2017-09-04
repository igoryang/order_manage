#order_manage

###写在前面  python djanog 练手项目
--Django项目：

--初始化mysql:   creater database order;   setttings.py  root/123.abc

--c:\Python27\python.exe manage.py syncdb  #1.9以上取消此命令

--django >1.9以上数据库操作
--c:\Python27\python.exe manage.py makemigratios
--c:\Python27\python.exe manage.py migrate

--c:\Python27\python.exe manage.py runnserver 0.0.0.0 8001

--admin-django startproject    -->  manage.py startapp  startproject



###设置 admin后台 admin.py中设置
--分类管理
--订单管理
--产品管理
list_display 添加显示字段内容
search_fields 添加快速查询栏
list_filter 过滤器
list_per_page 每个表记录分页显示 20/页


###欢迎使用 order  订单管理系统
--order_manage
--搭建环境：python 2.7 + django1.8.14 + mysql_5.6
**order ** 是一款由python编写开源的系统，django框架。
支持常见系统:
 1. redhat centos
 2. debian
 3. suse ubuntu
 4. freebsd
 5. windows



###截图： 设计页面预览：

首页

![webterminal](https://github.com/igoryang/order_manage/blob/master/page_design/front_001.png)

![webterminal](https://github.com/igoryang/order_manage/blob/master/page_design/order002.png)

![webterminal](https://github.com/igoryang/order_manage/blob/master/page_design/product002.png)


admin 后台管理

![webterminal](https://github.com/igoryang/order_manage/blob/master/page_design/admin_001.png)

![webterminal](https://github.com/igoryang/order_manage/blob/master/page_design/admin_type.png)

![webterminal](https://github.com/igoryang/order_manage/blob/master/page_design/admin_order.png)

![webterminal](https://github.com/igoryang/order_manage/blob/master/page_design/admin_product.png)








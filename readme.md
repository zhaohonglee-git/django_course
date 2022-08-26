### 
- https://docs.djangoproject.com/en/4.1/intro/
- 按照官方文档复现的工程，用于初步了解Django MTV设计模式
- If you’re using PostgreSQL, you’ll need the psycopg2 package.
- database: postgreSQL @django_webapp user: postgres 
- superuser: History password: History@21




#### something about can't compare datetime.datetime to datetime.date
- datetime.now() # 格式为 datetime.datetime
- datetime.datetime to datetime.date >> dt_datetime = datetime.now() # 格式为 datetime.datetime >> dt_date = datetime.date(dt_datetime)



### rest_framework 源码学习
- app  learning_restframework
- Django 中自带的响应器不是很好用，不能序列化显示数据 from django.http import HttpResponse
- rest_framework 中好用的响应器（序列化显示数据 Json） from rest_framework.response import Response  
- 

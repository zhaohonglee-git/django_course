### 
- https://docs.djangoproject.com/en/4.1/intro/
- 按照官方文档复现的工程，用于初步了解Django MTV设计模式
- database: postgreSQL @django_webapp user: postgres 
- superuser: History password: History@21
#### something about can't compare datetime.datetime to datetime.date
- datetime.now() # 格式为 datetime.datetime
- datetime.datetime to datetime.date >> dt_datetime = datetime.now() # 格式为 datetime.datetime >> dt_date = datetime.date(dt_datetime)

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
- http://www.yuan316.com/  博客地址
- app  learning_restframework
- 前后端职责分离的开发模式
- DRF 核心组件：序列化/反序列化组件、视图（views）组件
- 

##### something about serializers
- 序列化和反序列化，采用rest_framework 好用的响应器能够解码JSON OrderDict 等data格式
- Django 中自带的响应器不是很好用，不能序列化显示数据 from django.http import HttpResponse
- rest_framework 中好用的响应器（序列化显示数据 Json） from rest_framework.response import Response  
- from rest_framework import serializers   serializers
- serializers.Serializer (基础性序列化器) ☆
- serializers.ModelSerializer(基于模型类的序列化器) ☆☆
  
##### something about View class
- Djngo(View) ★ -->rest_framework(APIView) ★★ --> rest_framework(mixins and generics) ★★★  --> rest_framework(generics.RetrieveUpdateDestroyAPIView  Super) ★★★★
- from rest_framework import mixins and from rest_framework import generics  mixins and generics ★★★
  - mixins.ListModelMixin
  - mixins.CreateModelMixin
  - mixins.RetrieveModelMixin
  - mixins.UpdateModelMixin
  - mixins.DestroyModelMixin
- generics.RetrieveUpdateDestroyAPIView, generics.ListCreateAPIView ★★★★


### something else
- git checkout -b bug-fixes   建立分支并切换到该分支
- git checkout branch name  切换到已有分支
- git push origin local_branch_name:origin_branch_name
- git branch -a查看所有分支
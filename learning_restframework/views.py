from django.shortcuts import render
from .models import Student
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response

# Create your views here.

# Django View
class StudentView(View):
    model = Student

    def get(self, request):
        return HttpResponse("get...")

    def post(self, request):
        return HttpResponse("post...")


# rest_framework APIView
class StudentAPIView(APIView):
    model = Student

    def get(self, request):
        print(request.GET)
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        # return HttpResponse(f"rest_framework APIView get...")
        # HttpResponse 显示 OrderDict 格式而不是Json格式
        # return HttpResponse(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        # 将客户端输入的数据反序列化，并且做校验，校验成功则将数据写入数据库
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            print("post validation successful!")
            stu = Student.objects.create(**serializer.validated_data)
            ser = StudentSerializer(instance=stu, many=False)
            return Response(ser.data)
        else:
            return Response(serializer.errors)

        # return HttpResponse(
        #     f"rest_framework APIView post...",
        # )


# serialize the data
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    age = serializers.IntegerField()
    sex = serializers.CharField(source="gender")


class StudentDetailAPIView(APIView):
    def get(self, request, id):
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(instance=student, many=False)
        return Response(serializer.data)

    def delete(self, request, id):
        Student.objects.get(pk=id).delete()
        return Response()

    def put(self, request, id):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            print("post validation successful!")
            Student.objects.filter(pk=id).update(**serializer.validated_data)
            stu = Student.objects.get(id=id)
            ser = StudentSerializer(instance=stu, many=False)
            return Response(ser.data)
        else:
            return Response(serializer.errors)

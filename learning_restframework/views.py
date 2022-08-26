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
        return HttpResponse(
            f"rest_framework APIView post...",
        )


# serialize the data
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.CharField()

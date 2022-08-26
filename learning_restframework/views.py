from .models import Student
from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import serializers

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response


# Create your views here.
# CRRUD   增删改查查

########## Django View raw  ★  ##########
class StudentView(View):
    model = Student

    def get(self, request):
        return HttpResponse("get...")

    def post(self, request):
        return HttpResponse("post...")


########## rest_framework APIView  ★★  ##########
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


########## serialize the data raw ☆  ##########
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
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


########## Mixin ###############

# serializers.ModelSerializer ☆☆
class StudentModleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["age", "gender", "name"]


class StudentMixinAPIView(
    generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin
):

    queryset = Student.objects.all()
    serializer_class = StudentModleSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentMixinDetailAPIView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = Student.objects.all()
    serializer_class = StudentModleSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def delete(self, request, pk):
        return self.destroy(request)

    def put(self, request, pk):
        return self.update(request)


########### ListCreateAPIView extra Super ################
class StudentSuperAPIView(generics.ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentModleSerializer


class StudentSuperDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentModleSerializer

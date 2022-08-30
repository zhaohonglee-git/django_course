from urllib.request import parse_keqv_list
from django.shortcuts import render
from .models import Author, Book, Publish
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework import viewsets
from rest_framework.response import Response


############ raw serializers.Serializer + APIView  #####################


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    age = serializers.IntegerField()

    def create(self, validated_data):
        author_obj = Author.objects.create(**validated_data)

        return author_obj

    def update(self, instance, validated_data):
        Author.objects.filter(pk=instance.pk).update(**validated_data)

        # 注意必须返回这个object ，否则会报错，需要严格按照DRF源码的格式撰写
        return instance


# Create your views here.
class AuthorView(APIView):
    def get(slef, request):
        authors = Author.objects.all()
        s = AuthorSerializer(instance=authors, many=True)

        return Response(s.data)

    def post(slef, request):
        s = AuthorSerializer(data=request.data)

        # 数据校验,得到两个字典 serializer.validated_data 和 serializer.errors
        if s.is_valid():
            print("serializer.validated_data:", s.validated_data)

            # 向数据库添加记录
            # author_obj = Author.objects.create(**s.validated_data)
            # return Response("OK")

            # 或者调用save方法,将create等方法写入序列化器中，这样可以代码解耦
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)


class AuthorDetailView(APIView):
    def get(self, request, id):
        author = Author.objects.get(pk=id)
        s = AuthorSerializer(instance=author, many=False)

        return Response(s.data)

    def put(self, request, id):
        author = Author.objects.get(pk=id)
        s = AuthorSerializer(instance=author, data=request.data)

        # 数据校验
        if s.is_valid():
            # 更新逻辑，为了代码解耦，将这部分逻辑代码写入序列化的类中
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)

    def delete(self, request, id):
        Author.objects.get(pk=id).delete()
        return Response()


############ serializer.ModelSerializer + APIView #####################


class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"

    # 自定义校验，非常灵活
    def validate_name(self, value):

        if value.endswith("出版社"):
            return value
        else:
            raise serializers.ValidationError('出版社名称并未以"出版社"结尾')


class PublishView(APIView):
    def get(self, request):
        publishes = Publish.objects.all()
        s = PublishSerializer(instance=publishes, many=True)

        return Response(s.data)

    def post(self, request):
        s = PublishSerializer(data=request.data)

        # 使用ModelSerializer 时候没必要重写create等方法，因为ModelSerializer已经写好了，并且与特定的模型类进行了关联
        if s.is_valid():
            print("serializer.validated_data:", s.validated_data)

            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)


class PublishDetailView(APIView):
    def get(self, request, id):
        publish = Publish.objects.get(pk=id)
        s = PublishSerializer(instance=publish, many=False)

        return Response(s.data)

    def put(self, request, id):
        publish = Publish.objects.get(pk=id)
        s = PublishSerializer(instance=publish, data=request.data)

        # ModelSerializer中已经重写了对应的update方法，直接用save方法即可
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)

    def delete(self, request, id):
        Publish.objects.get(pk=id).delete()
        return Response()


############ GenericAPIView + serializers.ModelSerializer  利用多重继承解决get代码重复的问题  #####################
class PublishGenView(GenericAPIView):
    queryset = Publish.objects
    serializer_class = PublishSerializer

    def get(self, request):
        s = self.get_serializer(instance=self.get_queryset(), many=True)

        return Response(s.data)

    def post(self, request):
        s = self.get_serializer(data=request.data)

        if s.is_valid():
            print("serializer.validated_data:", s.validated_data)

            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)


class PublishGenDetailView(GenericAPIView):
    queryset = Publish.objects
    serializer_class = PublishSerializer

    def get(self, request, pk):
        s = self.get_serializer(instance=self.get_object(), many=False)
        return Response(s.data)

    def put(self, request, pk):
        s = self.get_serializer(instance=self.get_object(), data=request.data)

        if s.is_valid():
            print("serializer.validated_data:", s.validated_data)

            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)

    def delete(self, request, pk):
        self.get_object().delete()
        return Response()


############ mixins.ListModelMixin & mixins.CreateModelMixin ... + serializers.ModelSerializer  利用多重继承解决get代码重复的问题  #####################
# 多重继承
class PublishMixView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Publish.objects
    serializer_class = PublishSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PublishMixDetailView(
    GenericAPIView,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    queryset = Publish.objects
    serializer_class = PublishSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        self.destroy(request, pk)


############ 继续在以上的代码基础上封装（from rest_framework.generics import），将所有的继承类继续抽离到 ListCreateAPIView  RetrieveUpdateDestroyAPIView ############
class PublishSuperView(ListCreateAPIView):
    queryset = Publish.objects
    serializer_class = PublishSerializer


class PublishSuperDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Publish.objects
    serializer_class = PublishSerializer


############  viewSet版本 继续封装，封装到一个类中，用dispatch解决不同请求种类与执行方法映射 ############
# GET(查单个、查所有) POST PUT DELETE
# URL  .../publish/  --> GET 查所有
# URL  .../publish/3/  --> GET 查单个


class PublishSSView(viewsets.ModelViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer

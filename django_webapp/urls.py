"""django_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from learning_restframework.views import (
    StudentView,
    StudentAPIView,
    StudentDetailAPIView,
    StudentMixinAPIView,
    StudentMixinDetailAPIView,
    StudentSuperAPIView,
    StudentSuperDetailAPIView,
)
from viewApp.views import AuthorView, AuthorDetailView, PublishView, PublishDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("polls/", include("polls.urls")),
    path("student/", StudentView.as_view(), name="student"),
    path("studentapi/", StudentAPIView.as_view(), name="studentapi"),
    path(
        "studentapi/<int:id>/", StudentDetailAPIView.as_view(), name="studentapiDetail"
    ),
    path("studentmixinapi/", StudentMixinAPIView.as_view(), name="studentmixinapi"),
    path(
        "studentmixinapi/<int:pk>/",
        StudentMixinDetailAPIView.as_view(),
        name="studentmixinapiDetail",
    ),
    path("studentsuperapi/", StudentSuperAPIView.as_view(), name="studentsuperapi"),
    path(
        "studentsuperapi/<int:pk>/",
        StudentSuperDetailAPIView.as_view(),
        name="studentsuperapiDetail",
    ),
    path("authors/", AuthorView.as_view(), name="authors"),
    path("authors/<int:id>/", AuthorDetailView.as_view(), name="authorsDetail"),
    path("publishes/", PublishView.as_view(), name="publishes"),
    path("publishes/<int:id>/", PublishDetailView.as_view(), name="publishesDetail"),
]

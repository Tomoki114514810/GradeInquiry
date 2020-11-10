from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateUserView,GradeShowViewSet
from . import views



urlpatterns = [

    path('create/',CreateUserView.as_view(),name='create'),
    # path('teacher/',UploadView.as_view(),name='upload'),
    path('hogehoge/',GradeShowViewSet.as_view({'get':'list'})),
    path('authenticate/', include('djoser.urls.jwt'), )

]
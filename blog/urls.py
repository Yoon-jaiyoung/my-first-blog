from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),#post_list라는 view가 루트 URL에 할당
]
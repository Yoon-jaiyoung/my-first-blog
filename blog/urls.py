from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),#post_list라는 view가 루트 URL에 할당
    #post/ url에 post 문자를 포함
    #<int:pk> 장고 정수 값을 기대하고 pk
    #/ 다음에 /가 한번 더
    #결국, http://127.0.0.1:8000/post/5/ post_detail에서뷰를 찾음
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    path('post/new', views.post_new, name='post_new'),
    
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
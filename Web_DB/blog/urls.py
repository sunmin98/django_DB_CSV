from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    #URL에 파라미터로 넘어온 데이터를 id로 표시함
    #URL이름은 post_detail이고 views.post_detail와 매핑됫다
    path('post/create/',views.post_create,name='post_create'),
]
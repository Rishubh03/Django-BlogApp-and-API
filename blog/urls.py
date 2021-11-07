from django.urls import path
from django.views.generic.detail import DetailView
from .views import PostList,PostDetail

urlpatterns = [
    path('',PostList.as_view(),name = "home"),
    path('<slug:slug>/',PostDetail.as_view(), name='post_detail'),
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name = 'frontpage'),
    path('post<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post<int:pk>/update', PostUpdateView.as_view(), name = 'update'),
    path('post<int:pk>/delete', PostDeleteView.as_view(), name = 'delete'),
    path('about/', views.about, name='about'),
    path('publications/', views.public, name='publications'),



    #path('', views.frontpage, name='frontpage'),
    #path('about/', views.about, name='about'),
    #path('post_detail/<str:pk>', views.post_detail, name='post_detail'),


]

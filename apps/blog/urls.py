from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('publications/create/', views.CreatePostView.as_view(), name='post_create'),
    path('publications/<str:slug>/detail/', views.PostDetail.as_view(), name='post_detail'),
    path('leave-comment/', views.LeaveComment.as_view(), name='leave-comment'),
]
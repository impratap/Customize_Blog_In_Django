from django.urls import path
from . import views 
from .feeds import LatestPostsFeed

urlpatterns = [
    path('',views.PostList.as_view(), name = 'home'),
    path('about/',views.AboutPageView.as_view(), name='about'),
    path('privacy/',views.PrivacyPageView.as_view(), name='privacy'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
]


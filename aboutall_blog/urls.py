from django.urls import path, include
from . import views

app_name = 'aboutall_blog' # this name goes to html for separate names in aplications

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:post_id>/', views.detail, name='detail'), # passing post_id to func detail in views
]
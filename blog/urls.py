
from django.contrib import admin
from django.urls import path
from  home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('post',views.post,name='post'),
    path('blog',views.blog,name='blog'),

]

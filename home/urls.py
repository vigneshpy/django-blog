from django.urls import path
from  home import views
urlpatterns = [
    path('',views.home,name="index"),
    path('post',views.post,name="post")

    

]

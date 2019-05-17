
from django.contrib import admin
from django.urls import path
from  home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/<str:cat>',views.category,name="category"),
    path('',views.index,name="index"),
]

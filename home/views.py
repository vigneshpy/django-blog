from django.shortcuts import render


from admin_app.models import AddCategory
# Create your views here.


def index(request):
 
    return render(request,'index.html')


def  post(request):
   
   return render(request,'post.html')

def  blog(request):
   
   return render(request,'blog.html')


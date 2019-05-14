from django.shortcuts import render


from admin_app.models import AddCategory
# Create your views here.


def index(request):

    cat=AddCategory.objects.all()
    print(cat)
 
    return render(request,'index.html',{'list':cat})
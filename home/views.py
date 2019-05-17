from django.shortcuts import render


from admin_app.models import AddCategory
# Create your views here.


def index(request):

    cat=AddCategory.objects.all()[:5]
    print(cat)
 
    return render(request,'home.html',{'list':cat})


def  category(request,cat):
    cat1=AddCategory.objects.all()
    print(cat)
    return render(request,'category.html',{'categoryname':cat,'list':cat1})
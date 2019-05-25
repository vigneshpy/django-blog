from django.shortcuts import render



from django.http import HttpResponse
# Create your views here.


from .models import AddPost


def home(request):
	post=AddPost.objects.all().order_by('-id')[:3]
	return render(request,'index.html',{'list':post})

def post(request):



	return HttpResponse('Post')
def detail(request,id):
	post=AddPost.objects.get(id=id)

	print(post)

	return render(request,'post.html',{'list':post})


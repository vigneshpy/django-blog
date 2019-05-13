from django.db import models

# Create your models here.

class AddCategory(models.Model):
    category=models.CharField(max_length=40)
    description=models.CharField(max_length=120)
    created_date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
   
    def __str__(self):
        return self.category;


class AddPost(models.Model):
    title=models.CharField(max_length=130)
    body=models.TextField()
    posted_by=models.CharField(max_length=120,default='sss')
    slug=models.TextField()
    active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
   

    def __str__(self):

        return  self.title
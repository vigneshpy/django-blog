from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
# Create your models here.

class AddCategory(models.Model):
    category=models.CharField(max_length=40)

   
    def __str__(self):
        return self.category;


class AddPost(models.Model):
    category = models.ForeignKey(AddCategory, verbose_name="Category",on_delete=models.CASCADE)
    title=models.CharField(max_length=130)
    body=models.TextField()
    posted_by=models.CharField(max_length=120,default='sss')
    slug=models.TextField()
    active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
   

    def __str__(self):

        return  self.title
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(AddPost,self).save(*args,**kwargs)


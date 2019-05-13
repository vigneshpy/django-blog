from django.contrib import admin

from admin_app.models import AddCategory,AddPost
# Register your models here.


admin.site.site_header='Vigneshpy Blog || Admin'


class AddCategoryAdmin(admin.ModelAdmin):
    list_display = ('category','description')
    list_filter=('created_date','category',)
    search_fields=('category',)
# class AddPostAdmin(admin.ModelAdmin):
#     list_filter=('created_date','posted_by'.'active',)



class PostAdmin(admin.ModelAdmin):
    list_display=('title','body','posted_by','created_date','active',)
    list_filter=('posted_by','created_date','active',)
    search_fields=('title','body','posted_by')

admin.site.register(AddCategory,AddCategoryAdmin)
admin.site.register(AddPost,PostAdmin)
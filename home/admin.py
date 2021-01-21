from django.contrib import admin
from home.models import Catagory
from home.models import Image

# Register your models here.


# @admin.register(Catagory)
# @admin.register(Image)

class CatogoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']


class ImageAdmin(admin.ModelAdmin):
    # this is for display showing in admin 
    list_display = ['title', 'desc', 'date', 'images']
    # this is for edit particular option
    list_editable = ['date']
    # this is for pagination in admin panel   
    list_per_page = 5
    # this is for filter option by category
    list_filter = ['cat']


admin.site.register(Catagory, CatogoryAdmin)
admin.site.register(Image, ImageAdmin)

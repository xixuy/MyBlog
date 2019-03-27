from django.contrib import admin

# Register your models here.
from blog.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')


admin.site.register(Article,ArticleAdmin)

class ProductAdmin(admin.ModelAdmin):
    #设置模型字段，用于admin后台数据的表头设置
    list_display = ['id','name','weight','size','type']
    list_display.append('colored_type')
    search_fields = ['id','name','type__type_name']
    list_filter = ['name','type__type_name']
    #设置排序方式
    ordering = ['id']
    #在添加新数据时，设置可添加数据的字段
    fields = ['name','weight','size','type']
    #设置可读字段，在修改或新增数据时使其无法设置
    readonly_fields = ['name']

admin.site.register(Product,ProductAdmin)


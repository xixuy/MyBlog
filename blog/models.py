from django.db import models

# Create your models here.
from django.utils.html import format_html


class Article(models.Model):
    """新建表字段"""
    title=models.CharField('博客标题',max_length=150)
    category=models.CharField('博客标签',max_length=50,blank=True)
    content=models.TextField(blank=True,null=True)
    pub_date=models.DateTimeField('发布日期',auto_now_add=True,editable=True)
    update_time=models.DateTimeField('修改时间',auto_now=True,null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['-pub_date']
        verbose_name='文章'
        verbose_name_plural=verbose_name

#产品分类表
class Type(models.Model):
    id=models.AutoField(primary_key=True)
    type_name=models.CharField(max_length=20)

    def __str__(self):
        return self.type_name


class Product(models.Model):
    """新建表字段"""
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    weight=models.CharField(max_length=20,default="")
    size=models.CharField(max_length=20,default="")
    type=models.ForeignKey(Type,on_delete=models.CASCADE)
    #设置返回值
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='产品信息'
        verbose_name_plural=verbose_name

      #自定义函数，通过判断模型字段的数据内容，从而返回不同的字体颜色
    def colored_type(self):
        if '手机' in self.type.type_name:
            color_code='red'
        elif '平板电脑' in self.type.type_name:
            color_code='blue'
        elif '智能穿戴' in self.type.type_name:
            color_code = 'green'
        else:
            color_code='yellow'
        return format_html(
            '<span style="color:{};">{}</span>',
            color_code,
            self.type,
        )
    colored_type.short_description='带颜色的产品类型'


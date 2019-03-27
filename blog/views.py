from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from blog.models import *
from .form import *

def index(request):
    type=Type.objects.create(id=2,type_name='电脑')
    #创建数据
    # p=Product.objects.create(name='荣耀10',weight='121g',size='120*75*7mm',type_id=1,id=2)
    type.save()
    # p.save()
    #更行单条数据
    # u=Product.objects.get(id=1).update(name='华为荣耀V9')
    # u.save()
    # type_list=Product.objects.values('type').distinct()
    # name_list=Product.objects.values('name','type')
    # context={'title':"首页",
    #          'type_list':type_list,
    #          'name_list':name_list
    #          }
    return HttpResponse(request,'index.html')

def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        #绝对路径，完整的地址信息
        # return redirect('http://127.0.0.1:8000/')
        #相对路径，代表首页地址
        return redirect('/')
    else:
        if request.GET.get('name'):
            name=request.GET.get('name')
        else:
            name='Everyone'
        return HttpResponse('username is '+ name)


def product(request):
    #GET请求
    if request.method=='GET':

        product=ProdectForm()
        return render(request,'data_form.html',locals())
    else:
        product=ProdectForm(request.POST)
        if product.is_valid():
            #获取网页控件name的数据
            name=product['name']
            return HttpResponse('提交成功')
        else:
            #将错误信息输出，error_msg是将错误信息以json格式输出
            error_msg=product.errors.as_json()
            print(error_msg)
            return render(request,'data_form.html',locals())


def model_index(request, id):
    if request.method=='GET':
        instance=Product.objects.filter(id=id)

        if instance:
            product=ProductModelForm(instance=instance[0])
        else:
            product=ProductModelForm()
        return  render(request,'data_form.html',locals())
    else:
        product=ProductModelForm(request.POST)
        if product.is_valid():
            weight=product.cleaned_data['weight']
            product_db=product.save(commit=False)
            product_db.name='我的 iPhone'
            product_db.save()
            return HttpResponse('提交成功！weight清洗后的数据为：'+weight)
        else:
            error_msg=product.errors.as_json()
            print(error_msg)
            return render(request,'data_form.html',locals())
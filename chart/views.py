from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



# 折线图对应的的模板
def showlinediagram(request):
    return render(request, 'showline.html')

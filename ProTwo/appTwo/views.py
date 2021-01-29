from django.shortcuts import render
from .models import User
# Create your views here.



def index(request):
    return render(request,'index.html')


def user(request):
    user_list=User.objects.order_by('first_name')
    return render(request,'index.html',{'users':user_list})
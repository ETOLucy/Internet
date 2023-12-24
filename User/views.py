from django.shortcuts import render,redirect
from User.models import Users

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse


# 示例后端处理（使用 Django 框架）
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Drone.models import Drone
from User.models import Order
from decimal import Decimal
import json

# Create your views here.
def register(request):
    return render(request,'User/register.html')
def login(request):
    return render(request, "User/login.html")

def register(request):
    method = request.method # 请求方法
    if method == "GET":
        return render(request, "User/register.html")
    elif method == "POST":
        username = request.POST.get("username")
        res = Users.objects.filter(username=username)

        """验证用户名是否存在"""
        if res:
            messages.error(request,"该用户名已被注册，请尝试新的用户名。")
            return HttpResponseRedirect(reverse('user:register'))

        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        if(password!=repassword):
            messages.error(request,"两次密码不一致，请重新注册。")
            return HttpResponseRedirect(reverse('user:register'))

        phone = request.POST.get("phone")

        """添加数据"""
        Users.objects.create(phone=phone, username=username, password=password)

        messages.success(request,"恭喜，注册成功！")
        return HttpResponseRedirect(reverse('user:login'))
    
def login(request):
    method = request.method
    if method == "GET":
        return render(request, "User/login.html")
    elif method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = Users.objects.get(username=username)
            if password == user.password:
                request.session['username'] = user.username
                return redirect('../../index')

            else:
                # messages.add_message(request, messages.ERROR, '密码错误，请重新输入密码')
                messages.error(request,"密码错误，请重新输入密码。")
                return HttpResponseRedirect(reverse('user:login'))
            

        except Users.DoesNotExist:
            messages.error(request,"用户不存在，请重新登录。")
            return HttpResponseRedirect(reverse('user:login'))
        





# _*_ coding:utf-8 _*_
import re

from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q         # Q表示或【可用于手机或邮箱作为登录】
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend      # 通过邮箱登陆
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password        # 把明文密码加密
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.

from users.forms import UserForm
from users.models import EmailVerifyRecord
from choices.models import QuestionNaire
from users.other.email_send import send_register_email


# 问卷开始页面
class IndexView1(View):
    def get(self, request):
        return redirect('/users/')


# 问卷开始页面
class IndexView(View):
    def get(self, request):
        return render(request,'index.html')


# 重写authenticate方法，让用户可以用邮箱登录【setting 里要有对应的配置】
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 实现登录
class LoginView(View):

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'users/login.html', {'msg': '用户名或密码错误!'})


# 用户登出
class LogoutView(View):
    def get(self, request):
        logout(request)
        # if request.user.is_authenticated():
        #     return HttpResponse("You are logged in.")
        # else:
        #     return HttpResponse("You are not logged in.")
        return render(request, 'users/login.html')


# 用户注册
class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            errors = {}
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            # message = form.cleaned_data['message']
            UserFilter = User.objects.filter(username=username)
            if UserFilter:
                errors['username']='用户名已经存在'
                return render(request, 'users/register.html', {'errors': errors})
            elif password1 != password2:
                errors['password']='输入密码不一致'
                return render(request, 'users/register.html', {'errors': errors})
            else:
                user = User()
                user.username = username
                # user.email = message
                user.password = make_password(password1)
                user.is_active=False
                user.save()
                return render(request,'users/login.html',{})
        else:
            return render(request, 'users/register.html',{'form':form})


# 个人中心
class UsMessageView(View):
    def get(self, request):
        return render(request, 'users/UserMessage.html')


# 添加邮箱
class AddEmailView(View):
    def get(self, request):
        return render(request,'users/AddEmail.html')
    def post(self,request):
        user_email = request.POST.get('title','')
        user = User.objects.filter(email=user_email)
        if user:
            return render(request, 'users/AddEmail.html', {'error': '邮箱已经被绑定'})
        else:
            str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
            if not re.match(str, user_email):
                return render(request,'users/AddEmail.html',{'error':'邮箱格式输入错误'})
            else:
                user = request.user
                user.email = user_email
                user.is_active = False
                user.save()
                return render(request,'users/UserMessage.html')


# 激活邮箱
class ActiveEmailView(View):
    def get(self, request):
        user_email = request.user.email
        send_register_email(user_email, send_type="AddEmail")
        return render(request,'users/Active.html')


# 激活链接
class ActiveView(View):
    def get(self, request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                if record.send_type == "AddEmail":
                    users = User.objects.filter(email=record.email)
                    for user in users:
                        if request.user == user:
                            user.is_active = True
                            user.save()
                            return render(request,'users/UserMessage.html')
                elif record.send_type == "ForPass":
                    user = User.objects.get(email=record.email)
                    return render(request, 'users/SetPassword.html',{'user':user})
            return render(request, 'users/active_fail.html')
        else:
            return render(request, 'users/active_fail.html')


# 激活链接
class ForPassView(View):
    def get(self, request):
        return render(request, 'users/forgetpwd.html')

    def post(self, request):
        email = request.POST.get('title','')
        user = User.objects.get(email=email)
        if user:
            send_register_email(email, send_type="ForPass")
            return render(request, 'users/Active.html')
        else:
            return render(request, 'users/forgetpwd.html',{'error':'邮箱所属用户不存在'})


# 激活链接
class ChanPassView(View):
    def post(self, request,user_id):
        user = User.objects.get(id=user_id)
        user.password = make_password(request.POST['title'])
        user.save()
        return render(request, 'users/login.html')


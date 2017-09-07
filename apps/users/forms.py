# _*_ coding:utf-8 _*_
__author__ = 'zhuzhao'
__date__ = '2017/5/4 19:49'

from django import forms
# from captcha.fields import CaptchaField


class MyForm(forms.Form):
    text = forms.CharField(max_length=100)


class UserForm(forms.Form):
    username = forms.CharField(required=True,max_length=20)
    # message = forms.EmailField(max_length=20)
    password1 = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)
    # captcha = CaptchaField()
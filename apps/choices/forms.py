# _*_ coding:utf-8 _*_
__author__ = 'zhuzhao'
__date__ = '2017/5/9 12:25'

from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(max_length=20)
    content = forms.EmailField(max_length=20)
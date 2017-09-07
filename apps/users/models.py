# _*_ coding:utf-8 _*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class QuestionNaire(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title =  models.CharField(max_length=30,verbose_name="问卷名称")
    put_time = models.DateTimeField(verbose_name="添加时间")
    num = models.IntegerField(default=0,verbose_name='问卷被填写次数')

    class Meta:
        verbose_name='用户个人问卷'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.title


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=18, choices=(('register', '邮箱'), ('forget', '修改密码'), ('update_email', '修改邮箱')),verbose_name='验证码类型')
    send_time = models.DateField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = '邮箱验证码'
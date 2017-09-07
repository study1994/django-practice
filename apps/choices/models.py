# _*_ coding:utf-8 _*_
from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from users.models import QuestionNaire
from datetime import datetime


class MyQuestion(models.Model):
    question = models.ForeignKey(QuestionNaire,on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now(),verbose_name='添加时间')
    name = models.CharField(max_length=20,verbose_name='问题名')
    type = models.CharField(max_length=20,choices=(('1','单选题'),('2','多选题'),('3','填空题'),),null=True)
    orde = models.IntegerField(verbose_name='题目排序',default=0)

    class Meta:
        verbose_name=u'问题题目'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class MyChoice(models.Model):
    question = models.ForeignKey(MyQuestion,on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')
    name = models.CharField(max_length=20,verbose_name='选项')
    num = models.IntegerField(verbose_name='选择次数',default=0)

    class Meta:
        verbose_name=u'问题选项'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class MyText(models.Model):
    question = models.ForeignKey(MyQuestion,on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')
    name = models.TextField(max_length=20,verbose_name='文本内容',null=True,blank=True)

    class Meta:
        verbose_name=u'问题问答'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.question.name


class Content(models.Model):
    mytext = models.ForeignKey(MyText,on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')
    name = models.TextField(max_length=20,verbose_name='用户答案内容存储',null=True,blank=True)

    class Meta:
        verbose_name=u'问答题型填写'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class AnserTime(models.Model):
    question = models.ForeignKey(QuestionNaire, on_delete=models.CASCADE)
    anser_time=models.DateTimeField(default=datetime.now(), verbose_name='回答时间')

    class Meta:
        verbose_name=u'用户问卷填写时间'
        verbose_name_plural=verbose_name
# _*_ coding:utf-8 _*_
__author__ = 'zhuzhao'
__date__ = '2017/5/16 19:41'


# _*_ coding:utf-8 _*_
from django.conf.urls import patterns, include, url
from django.contrib import admin

from choices.views import QuNaReleaseView,QuNaAddView,QuNairedelectView,QuNaResultView,QuNaEditView,QuNaDetailView,QuNaAdd1View
from choices.views import QuMoveView,QuAddView,QuDelectView,ChoiceAddView,ChoiceDelectView


urlpatterns = patterns('',
    # 查看问卷
    url(r'^quna_detail/(?P<quna_id>\d+)/$', QuNaDetailView.as_view(), name='QuNaDetail'),
    # 发布问卷
    url(r'^quna_release/(?P<quna_id>\d+)/$', QuNaReleaseView.as_view(),name='QuNaRelease'),
    # # 添加问卷
    # url(r'^quna_add/$',QuNaAddView.as_view(), name='QuNaAdd'),
    # 添加问卷
    url(r'^quna_add1/$',QuNaAdd1View.as_view(), name='QuNaAdd1'),
    # 删除问卷
    url(r'^quna_delect/(?P<quna_id>\d+)/$', QuNairedelectView.as_view(), name='QuNaDelect'),
    # 统计结果
    url(r'^quna_result/(?P<quna_id>\d+)/$',QuNaResultView.as_view(),name='QuNaResult'),
    # 问卷编辑
    url(r'^quna_edit/(?P<quna_id>\d+)/$', QuNaEditView.as_view(),name='QuNaEdit'),


    # 题目上下移动
    url(r'^questionn_move/(?P<qu_id>\d+)/(?P<my_id>\d+)/$', QuMoveView.as_view(),name='QuMove'),
    # 添加题目
    url(r'^questionn_add/(?P<quna_id>\d+)/(?P<choice>\w+)/$', QuAddView.as_view(),name='QuAdd'),
    # 删除题目
    url(r'^questionn_delect/(?P<quna_id>\d+)/(?P<qu_id>\d+)/$',QuDelectView.as_view(), name='QuDelect'),
    # 添加问题选项
    url(r'^choice_add/(?P<quna_id>\d+)/(?P<qu_id>\d+)/$',ChoiceAddView.as_view(), name='ChoiceAdd'),
    # 删除问题选项
    url(r'^choice_delect/(?P<quna_id>\d+)/(?P<answer_id>\d+)/$',ChoiceDelectView.as_view(), name='ChoiceDelect'),

)
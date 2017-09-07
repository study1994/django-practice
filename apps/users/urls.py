# _*_ coding:utf-8 _*_
__author__ = 'zhuzhao'
__date__ = '2017/5/16 19:41'


from django.conf.urls import patterns, url
from users.views import IndexView,LoginView,LogoutView,RegisterView,UsMessageView,AddEmailView,ActiveEmailView,ActiveView, ForPassView,ChanPassView

urlpatterns = patterns('',
    # 问卷主页
    url(r'^$', IndexView.as_view(), name='index'),

    # 用户登录，登出，注册
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),

    url(r'^user_message/$', UsMessageView.as_view(), name='UsMessage'),
    url(r'^add_email/$', AddEmailView.as_view(), name='AddEmail'),
    url(r'^active_email/$', ActiveEmailView.as_view(), name='ActiveEmail'),
    url(r'^active/(?P<active_code>.*)/$', ActiveView.as_view(), name='user_active'),
    url(r'^forgot_password/$', ForPassView.as_view(), name='ForPass'),
    url(r'^change_password/(?P<user_id>\d+)/$', ChanPassView.as_view(), name='ChanPass'),
)
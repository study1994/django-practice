# _*_ coding:utf-8 _*_
from django.conf.urls import patterns, include, url
from django.contrib import admin

from users.views import IndexView1
from choices.api import quna,quna_list
from rest_framework.authtoken import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Survey_project_0.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 问卷主页
    url(r'^$', IndexView1.as_view(), name='index'),
    # 验证码
    # url(r'^captcha/', include('captcha.urls')),

    # 其他App页面
    url(r'^users/', include('users.urls',namespace='users')),
    url(r'^choices/', include('choices.urls',namespace='choices')),

    url(r'^quna_list/',quna_list),
    url(r'^api/quna_list/',quna,name='qunalist'),
    url(r'^api/token-auth$',views.obtain_auth_token),
)

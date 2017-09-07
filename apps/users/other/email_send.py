# _*_ coding:utf-8 _*_
__author__ = 'zhuzhao'
__date__ = '2017/5/24 18:56'

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from Survey_project_0.settings import EMAIL_FROM


# 随机生成字符串
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


# 注册激活，密码重置，邮箱修改
def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "AddEmail":
        email_title = "问卷邮箱激活、添加链接"
        email_body = "请点击下面的链接激活你的邮箱: http://127.0.0.1:8000/users/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'ForPass':
        email_title = "问卷调查密码找回链接"
        email_body = "请点击下面的链接重置你的密码: http://127.0.0.1:8000/users/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
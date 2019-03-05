import os
from django.core.mail import send_mail
from untitled1 import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'untitled1.settings'

if __name__ == '__main__':

    send_mail(
        '来自www.liujiangblog.com的测试邮件',
        '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，本站专注于Python和Django技术的分享！',
        'xxx@sina.com',
        ['347202084@qq.com'],
    )
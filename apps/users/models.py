# coding:utf-8

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True


class UserProfile(AbstractUser, BaseModel):
    nick_name = models.CharField(verbose_name="昵称", null=True, default='', max_length=50)
    birthday = models.DateTimeField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=10)
    address = models.CharField(verbose_name="地址", default='', max_length=100)
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    image = models.ImageField(verbose_name="用户头像", upload_to='head_image/%Y/%m', default='default.jpg')
    signature = models.CharField(verbose_name="个性签名", null=True, blank=True, max_length=200)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username



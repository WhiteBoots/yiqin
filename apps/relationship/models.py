# coding:utf-8

from django.db import models
from apps.users.models import UserProfile, BaseModel


class Friends(BaseModel):
    user_you = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="主用户", related_name="user_you")
    user_other = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="其他用户", related_name="user_other")

    class Meta:
        verbose_name = '好友'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} and {}'.format(self.user_you, self.user_other)


class FriendsGroups(BaseModel):
    user = models.ManyToManyField(UserProfile, verbose_name="用户")
    name = models.CharField(verbose_name="组群名字", max_length=100, unique=True)
    desc = models.TextField(verbose_name="组群简介", max_length=300, default="", null=True)

    class Meta:
        verbose_name = '组群'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


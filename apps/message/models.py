# coding:utf-8

from django.db import models
from apps.users.models import BaseModel, UserProfile
from apps.relationship.models import FriendsGroups


class UserDynamic(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    title = models.CharField(verbose_name="动态标题", max_length=100, default='无标题')
    content = models.TextField(verbose_name="动态正文", max_length=300)
    likes = models.IntegerField(verbose_name="点赞数", default=0)

    class Meta:
        verbose_name = '用户动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}:{}'.format(self.user, self.title)


class UserDynamicImage(BaseModel):
    user_dynamic = models.ForeignKey(UserDynamic, on_delete=models.CASCADE, verbose_name="用户动态")
    image = models.ImageField(verbose_name="动态图片", upload_to='dynamic_image/%Y/%m', default='', null=True)

    class Meta:
        verbose_name = '动态图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image.url


class UserDynamicLikes(BaseModel):
    user_dynamic = models.ForeignKey(UserDynamic, on_delete=models.CASCADE, verbose_name="用户动态")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="点赞用户")

    class Meta:
        verbose_name = '动态点赞'
        verbose_name_plural = verbose_name


class UserDynamicComment(BaseModel):
    user_dynamic = models.ForeignKey(UserDynamic, on_delete=models.CASCADE, verbose_name="用户动态")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="评论用户")
    comment = models.CharField(verbose_name="评论内容", max_length=300)

    class Meta:
        verbose_name = '动态评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment


class UserMessages(BaseModel):
    user_send = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="发送方用户",
                                  related_name="user_send")
    user_reserve = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="接收方用户",
                                     related_name="user_reserve")
    content = models.TextField(verbose_name="文本内容", max_length=500, null=True, blank=True)
    message_type = models.CharField(verbose_name="消息类型", max_length=20,
                                    choices=(("1", "文本"), ("2", "图片"), ("3", "文件")))

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}->{}'.format(self.user_send, self.user_reserve)

        # if self.content:
        #     return self.content
        # else:
        #     return 'message_type: {}'.format(self.message_type)


class UserMessagesImage(BaseModel):
    user_messages = models.ForeignKey(UserMessages, on_delete=models.CASCADE, verbose_name="用户")
    image = models.ImageField(verbose_name="用户消息图片", upload_to='user_message_image/%Y/%m')

    class Meta:
        verbose_name = '用户消息图片'
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.image


class UserMessagesFile(BaseModel):
    user_messages = models.ForeignKey(UserMessages, on_delete=models.CASCADE, verbose_name="用户")
    file = models.FileField(verbose_name="用户消息文件", upload_to='user_message_file/%Y/%m')

    class Meta:
        verbose_name = '用户消息文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.file


class GroupMessages(BaseModel):
    user_send = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="发送方用户")
    user_group = models.ForeignKey(FriendsGroups, on_delete=models.CASCADE, verbose_name="接收方组群")
    content = models.TextField(verbose_name="文本内容", max_length=500, default='', null=True)
    message_type = models.CharField(verbose_name="消息类型", max_length=20,
                                    choices=(("1", "文本"), ("2", "图片"), ("3", "文件")))

    class Meta:
        verbose_name = '组群消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}->{}'.format(self.user_send, self.user_group)

        # if self.content:
        #     return self.content
        # else:
        #     return 'message_type: {}'.format(self.message_type)


class GroupMessagesImage(BaseModel):
    group_messages = models.ForeignKey(GroupMessages, on_delete=models.CASCADE, verbose_name="组")
    image = models.ImageField(verbose_name="用户消息图片", upload_to='group_message_image/%Y/%m')

    class Meta:
        verbose_name = '组群消息图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image


class GroupMessagesFile(BaseModel):
    group_messages = models.ForeignKey(GroupMessages, on_delete=models.CASCADE, verbose_name="组")
    file = models.FileField(verbose_name="组群消息文件", upload_to='user_message_file/%Y/%m')

    class Meta:
        verbose_name = '组群消息文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.file

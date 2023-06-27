# coding:utf-8

from django.contrib import admin
from apps.message.models import UserDynamic, UserDynamicImage, UserDynamicLikes, UserDynamicComment, UserMessages, \
    UserMessagesImage, UserMessagesFile, GroupMessages, GroupMessagesImage, GroupMessagesFile


class UserDynamicAdmin(admin.ModelAdmin):
    fields = ["user", "title", "content", "likes"]
    list_display = ["user", "title", "content", "likes"]


class UserDynamicImageAdmin(admin.ModelAdmin):
    fields = ["user_dynamic", "image"]
    list_display = ["user_dynamic", "image"]


class UserDynamicLikesAdmin(admin.ModelAdmin):
    fields = ["user_dynamic", "user"]
    list_display = ["user_dynamic", "user"]


class UserDynamicCommentAdmin(admin.ModelAdmin):
    fields = ["user_dynamic", "user", "comment"]
    list_display = ["user_dynamic", "user", "comment"]


class UserMessagesImageInline(admin.TabularInline):
    model = UserMessagesImage
    extra = 0


class UserMessagesFileInline(admin.TabularInline):
    model = UserMessagesFile
    extra = 0


class UserMessagesAdmin(admin.ModelAdmin):
    fields = ["user_send", "user_reserve", "content", "message_type"]
    list_display = ["user_send", "user_reserve", "content", "message_type"]
    inlines = [
        UserMessagesImageInline,
        UserMessagesFileInline,
    ]


class UserMessagesImageAdmin(admin.ModelAdmin):
    fields = ["image"]
    list_display = ["image"]


class UserMessagesFileAdmin(admin.ModelAdmin):
    fields = ["file"]
    list_display = ["file"]


class GroupMessagesFileInline(admin.TabularInline):
    model = GroupMessagesFile
    extra = 0


class GroupMessagesImageInline(admin.TabularInline):
    model = GroupMessagesImage
    extra = 0


class GroupMessagesAdmin(admin.ModelAdmin):
    fields = ["user_send", "user_group", "content", "message_type"]
    list_display = ["user_send", "user_group", "content", "message_type"]
    inlines = [
        GroupMessagesImageInline,
        GroupMessagesFileInline,
    ]

class GroupMessagesImageAdmin(admin.ModelAdmin):
    fields = ["image"]
    list_display = ["image"]


class GroupMessagesFileAdmin(admin.ModelAdmin):
    fields = ["file"]
    list_display = ["file"]


admin.site.register(UserDynamic, UserDynamicAdmin)
admin.site.register(UserDynamicImage, UserDynamicImageAdmin)
admin.site.register(UserDynamicLikes, UserDynamicLikesAdmin)
admin.site.register(UserDynamicComment, UserDynamicCommentAdmin)
admin.site.register(UserMessages, UserMessagesAdmin)
# admin.site.register(UserMessagesImage, UserMessagesImageAdmin)
# admin.site.register(UserMessagesFile, UserMessagesFileAdmin)
admin.site.register(GroupMessages, GroupMessagesAdmin)
# admin.site.register(GroupMessagesImage, GroupMessagesImageAdmin)
# admin.site.register(GroupMessagesFile, GroupMessagesFileAdmin)


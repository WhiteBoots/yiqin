# coding:utf-8

from django.contrib import admin
from apps.users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    fields = ["username", "nick_name", "password", "is_superuser", "is_staff", "is_active", "add_time", "last_login",
              "email", "birthday", "gender", "address", "mobile", "image", "signature"]
    list_display = ["username", "nick_name", "is_superuser", "is_active", "email", "mobile", "last_login"]


admin.site.register(UserProfile, UserProfileAdmin)

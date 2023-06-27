# coding:utf-8

from django.contrib import admin
from apps.relationship.models import Friends, FriendsGroups


class FriendsAdmin(admin.ModelAdmin):
    fields = ["user_you", "user_other", "add_time"]
    list_display = ["user_you", "user_other", "add_time"]


class FriendsGroupsAdmin(admin.ModelAdmin):
    fields = ["name", "desc", "add_time", "user"]
    list_display = ["name", "desc", "add_time"]
    filter_horizontal = ('user', )


admin.site.register(Friends, FriendsAdmin)
admin.site.register(FriendsGroups, FriendsGroupsAdmin)

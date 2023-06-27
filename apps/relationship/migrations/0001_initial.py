# Generated by Django 4.2.2 on 2023-06-27 02:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Friends",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "add_time",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="添加时间"
                    ),
                ),
            ],
            options={
                "verbose_name": "好友",
                "verbose_name_plural": "好友",
            },
        ),
        migrations.CreateModel(
            name="FriendsGroups",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "add_time",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="添加时间"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="组群名字"),
                ),
                (
                    "desc",
                    models.CharField(
                        default="", max_length=300, null=True, verbose_name="组群简介"
                    ),
                ),
            ],
            options={
                "verbose_name": "组群",
                "verbose_name_plural": "组群",
            },
        ),
    ]
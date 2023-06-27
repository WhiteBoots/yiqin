# Generated by Django 4.2.2 on 2023-06-27 07:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0009_usermessagesfile_usermessagesimage_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermessagesfile",
            name="user_messages",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="message.usermessages",
                verbose_name="用户",
            ),
        ),
        migrations.AlterField(
            model_name="usermessagesimage",
            name="user_messages",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="message.usermessages",
                verbose_name="用户",
            ),
        ),
        migrations.CreateModel(
            name="GroupMessagesImage",
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
                    "image",
                    models.ImageField(
                        upload_to="group_message_image/%Y/%m", verbose_name="用户消息图片"
                    ),
                ),
                (
                    "user_messages",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="message.usermessages",
                        verbose_name="用户",
                    ),
                ),
            ],
            options={
                "verbose_name": "组群消息图片",
                "verbose_name_plural": "组群消息图片",
            },
        ),
        migrations.CreateModel(
            name="GroupMessagesFile",
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
                    "file",
                    models.FileField(
                        upload_to="user_message_file/%Y/%m", verbose_name="组群消息文件"
                    ),
                ),
                (
                    "user_messages",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="message.usermessages",
                        verbose_name="用户",
                    ),
                ),
            ],
            options={
                "verbose_name": "组群消息文件",
                "verbose_name_plural": "组群消息文件",
            },
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0005_alter_userdynamiccomment_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermessages",
            name="content",
            field=models.TextField(
                default="", max_length=500, null=True, verbose_name="文本内容"
            ),
        ),
    ]

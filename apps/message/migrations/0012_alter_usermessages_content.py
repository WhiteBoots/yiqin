# Generated by Django 4.2.2 on 2023-06-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0011_alter_groupmessagesfile_user_messages_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermessages",
            name="content",
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name="文本内容"
            ),
        ),
    ]

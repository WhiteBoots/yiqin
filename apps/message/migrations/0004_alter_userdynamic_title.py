# Generated by Django 4.2.2 on 2023-06-27 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0003_userdynamic_title_alter_userdynamic_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdynamic",
            name="title",
            field=models.CharField(default="无标题", max_length=100, verbose_name="动态标题"),
        ),
    ]

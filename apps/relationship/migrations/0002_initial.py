# Generated by Django 4.2.2 on 2023-06-27 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("relationship", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="friendsgroups",
            name="user",
            field=models.ManyToManyField(
                to=settings.AUTH_USER_MODEL, verbose_name="用户"
            ),
        ),
        migrations.AddField(
            model_name="friends",
            name="user_other",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_other",
                to=settings.AUTH_USER_MODEL,
                verbose_name="其他用户",
            ),
        ),
        migrations.AddField(
            model_name="friends",
            name="user_you",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_you",
                to=settings.AUTH_USER_MODEL,
                verbose_name="主用户",
            ),
        ),
    ]
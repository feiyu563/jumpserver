# Generated by Django 2.1.7 on 2019-09-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0038_auto_20190911_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='authbook',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
        ),
    ]

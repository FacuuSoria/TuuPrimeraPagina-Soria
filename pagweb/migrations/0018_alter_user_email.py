# Generated by Django 4.2.4 on 2023-09-01 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagweb', '0017_rename_name_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
    ]
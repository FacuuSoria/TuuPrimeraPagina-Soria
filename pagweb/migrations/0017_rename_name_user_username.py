# Generated by Django 4.2.4 on 2023-09-01 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagweb', '0016_alter_post_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]

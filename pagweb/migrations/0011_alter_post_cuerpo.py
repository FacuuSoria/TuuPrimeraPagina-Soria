# Generated by Django 4.2.4 on 2023-08-31 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagweb', '0010_rename_descripcion_post_cuerpo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cuerpo',
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagweb', '0009_post_descripcion_post_link_alter_profesor_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='descripcion',
            new_name='cuerpo',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='subtitle',
            new_name='subtitulo',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='link',
        ),
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='post_imagen/'),
        ),
    ]

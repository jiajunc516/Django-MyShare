# Generated by Django 3.0.2 on 2020-02-18 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20200215_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]

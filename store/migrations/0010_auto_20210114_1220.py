# Generated by Django 3.1.3 on 2021-01-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210111_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
    ]

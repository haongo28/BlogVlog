# Generated by Django 2.0.3 on 2018-04-10 12:30

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20180410_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='topbanner',
            field=models.FileField(upload_to=blog.models.get_topbanner_filename),
        ),
    ]

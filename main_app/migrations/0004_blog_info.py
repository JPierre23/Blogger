# Generated by Django 4.0.6 on 2022-07-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_blog_date_blog_img_blog_tags_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='info',
            field=models.CharField(default='Test', max_length=2000),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-31 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARTICLE_app', '0012_topic_body_2_topic_title2'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image2',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
    ]
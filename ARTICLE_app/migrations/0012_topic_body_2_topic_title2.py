# Generated by Django 4.0.4 on 2022-05-31 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARTICLE_app', '0011_topic_2_body2_topic_2_image2_topic_2_title2'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='body_2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='title2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

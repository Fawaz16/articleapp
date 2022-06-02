# Generated by Django 4.0.4 on 2022-05-30 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='blog_image')),
            ],
        ),
    ]

# Generated by Django 3.2.23 on 2024-02-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='../default-blog.png', upload_to='images/', verbose_name='Image'),
        ),
    ]

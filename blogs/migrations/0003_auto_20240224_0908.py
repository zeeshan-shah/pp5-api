# Generated by Django 3.2.23 on 2024-02-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, max_length=4000, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='../default_blog_hcaioi.png', upload_to='images/', verbose_name='Image'),
        ),
    ]
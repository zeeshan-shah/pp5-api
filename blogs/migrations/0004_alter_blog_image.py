# Generated by Django 3.2.23 on 2024-02-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20240224_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='../default_blog_hcaioi', upload_to='images/', verbose_name='Image'),
        ),
    ]
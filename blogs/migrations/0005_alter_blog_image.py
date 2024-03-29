# Generated by Django 3.2.23 on 2024-02-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0004_alter_blog_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                default="../default-blog",
                upload_to="images/",
                verbose_name="Image",
            ),
        ),
    ]

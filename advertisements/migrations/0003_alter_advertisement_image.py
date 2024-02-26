# Generated by Django 3.2.23 on 2024-02-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("advertisements", "0002_advertisement_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advertisement",
            name="image",
            field=models.ImageField(
                default="../ad-here.jpg",
                upload_to="images/",
                verbose_name="Image",
            ),
        ),
    ]

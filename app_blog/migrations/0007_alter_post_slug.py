# Generated by Django 4.1.3 on 2022-11-27 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_blog", "0006_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]

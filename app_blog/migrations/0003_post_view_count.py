# Generated by Django 4.1.3 on 2022-11-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_blog", "0002_tag_post_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="view_count",
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-14 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="author",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="post.author"
            ),
        ),
    ]

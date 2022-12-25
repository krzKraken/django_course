# Generated by Django 4.1.4 on 2022-12-25 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("short_description", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("stock", models.IntegerField(default=20)),
            ],
        ),
    ]
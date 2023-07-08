# Generated by Django 4.2.2 on 2023-07-02 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Field",
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
                ("owner_id", models.IntegerField()),
                ("name", models.CharField(max_length=50)),
                (
                    "category_sport",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Футбол"),
                            (2, "Баскетбол"),
                            (3, "Воллейбол"),
                            (4, "Теннис"),
                        ]
                    ),
                ),
                ("location", models.FloatField()),
                ("time_from", models.IntegerField()),
                ("time_to", models.IntegerField()),
                ("description", models.TextField(max_length=300)),
                ("price", models.CharField(max_length=255)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("dimensions", models.CharField(max_length=100)),
                (
                    "surface_type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Натуральное"),
                            (2, "Искусственный газон"),
                            (3, "Паркет"),
                        ]
                    ),
                ),
                ("capacity", models.IntegerField(blank=True, null=True)),
                ("facilities", models.CharField(blank=True, max_length=255, null=True)),
                ("lighting", models.TextField(blank=True, null=True)),
                ("rules", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]

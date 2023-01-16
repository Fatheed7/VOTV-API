# Generated by Django 4.1.5 on 2023-01-16 21:14

from django.db import migrations, models
import sortedm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("keywords", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("cNumber", models.IntegerField()),
                ("cDesc", models.CharField(max_length=100)),
                ("cDesc_Upgrade", models.CharField(max_length=100)),
                (
                    "cRarity",
                    models.CharField(
                        choices=[
                            ("Common", "Common"),
                            ("Uncommon", "Uncommon"),
                            ("Rare", "Rare"),
                            ("Affliction", "Affliction"),
                        ],
                        max_length=20,
                    ),
                ),
                ("cType", models.IntegerField()),
                ("cName", models.CharField(max_length=100)),
                ("cEnergy", models.IntegerField()),
                ("cEnergy_Upgrade", models.IntegerField()),
                (
                    "keywords",
                    sortedm2m.fields.SortedManyToManyField(
                        blank=True,
                        help_text=None,
                        related_name="cards",
                        to="keywords.keywords",
                    ),
                ),
            ],
            options={
                "ordering": ["cNumber"],
            },
        ),
    ]

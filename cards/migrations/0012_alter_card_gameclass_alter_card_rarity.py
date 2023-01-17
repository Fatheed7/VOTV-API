# Generated by Django 4.1.5 on 2023-01-17 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0011_alter_card_description_alter_card_gameclass_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="gameClass",
            field=models.CharField(
                choices=[
                    ("The Enlightened", "The Enlightened"),
                    ("The Daughter of the Void", "The Daughter of the Void"),
                    ("Global", "Global"),
                    ("The Tempest", "The Tempest"),
                    ("The Hidden", "The Hidden"),
                ],
                default="Global",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="card",
            name="rarity",
            field=models.CharField(
                choices=[
                    ("Rare", "Rare"),
                    ("Affliction", "Affliction"),
                    ("Uncommon", "Uncommon"),
                    ("Common", "Common"),
                ],
                default="Common",
                max_length=100,
            ),
        ),
    ]

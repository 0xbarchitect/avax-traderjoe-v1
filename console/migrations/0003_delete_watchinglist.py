# Generated by Django 5.0.6 on 2024-08-03 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("console", "0002_position_liquidated_at"),
    ]

    operations = [
        migrations.DeleteModel(
            name="WatchingList",
        ),
    ]

# Generated by Django 4.2 on 2023-10-31 00:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rrapp", "0006_alter_listing_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 31, 0, 24, 1, 823620, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]

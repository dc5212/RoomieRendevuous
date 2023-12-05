# Generated by Django 4.2 on 2023-12-04 18:23

from django.db import migrations, models
import rrapp.models


class Migration(migrations.Migration):
    dependencies = [
        ("rrapp", "0016_merge_20231204_1146"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="question2",
            field=models.IntegerField(
                choices=[
                    (
                        1,
                        "Wait for that paycheck – you'll just have to spend as little as possible until then.",
                    ),
                    (
                        2,
                        "Ask your roommate for a small loan and pay him/her back when you get your paycheck.",
                    ),
                    (
                        3,
                        "Ask your roommate for a small loan,and pay him/her back in installments.",
                    ),
                    (
                        4,
                        "Take some money out of your roommate's top drawer and return it as soon as you get your pay.",
                    ),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to=rrapp.models.user_directory_path
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="rating",
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
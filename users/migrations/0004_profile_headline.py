# Generated by Django 3.2 on 2021-05-01 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_friendrequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="headline",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

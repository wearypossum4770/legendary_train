# Generated by Django 3.2 on 2021-05-04 17:06

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0002_lead_remote_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="employer_overview",
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hftcheckin', '0015_auto_20210526_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='pruefung',
            name='teilnahme',
            field=models.BooleanField(default=False),
        ),
    ]

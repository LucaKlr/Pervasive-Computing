# Generated by Django 3.2.3 on 2021-05-27 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hftcheckin', '0016_pruefung_teilnahme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pruefung',
            name='teilnahme',
        ),
    ]

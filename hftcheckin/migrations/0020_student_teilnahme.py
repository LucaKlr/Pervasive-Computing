# Generated by Django 3.2.3 on 2021-06-05 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hftcheckin', '0019_delete_studentschreibtpruefung'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teilnahme',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.2 on 2021-04-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hftcheckin', '0002_auto_20210422_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=45)),
                ('vorname', models.CharField(max_length=45)),
                ('nachname', models.CharField(max_length=45)),
            ],
        ),
    ]

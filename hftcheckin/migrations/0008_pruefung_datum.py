# Generated by Django 3.1.7 on 2021-05-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):
 
    dependencies = [
        ('hftcheckin', '0007_auto_20210518_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='pruefung',
            name='datum',
            field=models.CharField(max_length=45, null=True),
        ),
    ]

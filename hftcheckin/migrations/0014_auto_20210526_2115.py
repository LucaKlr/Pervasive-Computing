# Generated by Django 3.2.3 on 2021-05-26 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hftcheckin', '0013_professor_pruefung'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='pruefung',
        ),
        migrations.AddField(
            model_name='pruefung',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hftcheckin.professor'),
        ),
    ]

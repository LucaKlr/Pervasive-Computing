# Generated by Django 3.2.3 on 2021-06-05 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hftcheckin', '0017_remove_pruefung_teilnahme'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSchreibtPruefung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pruefung', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hftcheckin.pruefung')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hftcheckin.student')),
            ],
        ),
    ]

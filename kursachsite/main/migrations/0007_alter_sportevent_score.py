# Generated by Django 3.2.10 on 2021-12-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_sportevent_normalized_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportevent',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Баллы студента'),
        ),
    ]

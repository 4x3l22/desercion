# Generated by Django 5.1.6 on 2025-02-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdesercion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='documento',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]

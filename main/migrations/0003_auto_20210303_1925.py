# Generated by Django 3.1.4 on 2021-03-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210303_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='percentage',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
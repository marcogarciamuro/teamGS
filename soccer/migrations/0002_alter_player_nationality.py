# Generated by Django 4.2.5 on 2023-10-03 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='nationality',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

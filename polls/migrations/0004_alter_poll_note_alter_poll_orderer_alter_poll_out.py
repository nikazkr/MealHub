# Generated by Django 4.0.3 on 2022-03-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_poll_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='orderer',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='out',
            field=models.BooleanField(null=True),
        ),
    ]

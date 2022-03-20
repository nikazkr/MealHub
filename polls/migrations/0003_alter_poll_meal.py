# Generated by Django 4.0.3 on 2022-03-17 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_poll_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='meal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poll', to='polls.food'),
        ),
    ]
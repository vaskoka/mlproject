# Generated by Django 4.0.2 on 2022-10-23 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mltoolapp', '0006_clabject_instanceof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clabject',
            name='clabject',
        ),
        migrations.RemoveField(
            model_name='clabject',
            name='instanceOf',
        ),
        migrations.AddField(
            model_name='clabject',
            name='instanceOf',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instance', to='mltoolapp.clabject'),
        ),
    ]

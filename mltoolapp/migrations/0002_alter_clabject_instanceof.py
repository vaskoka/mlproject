# Generated by Django 4.1.2 on 2022-10-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mltoolapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clabject',
            name='instanceOf',
            field=models.ManyToManyField(null=True, to='mltoolapp.clabject'),
        ),
    ]

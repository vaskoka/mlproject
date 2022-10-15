# Generated by Django 4.1.2 on 2022-10-14 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mltoolapp', '0004_alter_clabject_clabject_alter_clabject_subclassof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clabject',
            name='clabject',
            field=models.OneToOneField(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classobject', to='mltoolapp.clabject'),
        ),
        migrations.AlterField(
            model_name='clabject',
            name='subclassOf',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subclass', to='mltoolapp.clabject'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-27 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_monitorcrt_pixqty_alter_monitorflat_pixqty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitorcrt',
            old_name='pixQty',
            new_name='picQty',
        ),
        migrations.RenameField(
            model_name='monitorflat',
            old_name='pixQty',
            new_name='picQty',
        ),
    ]

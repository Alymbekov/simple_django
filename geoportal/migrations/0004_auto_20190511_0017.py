# Generated by Django 2.2.1 on 2019-05-10 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoportal', '0003_auto_20190511_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worldborder',
            old_name='geometry',
            new_name='mpoly',
        ),
    ]
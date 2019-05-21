# Generated by Django 2.2.1 on 2019-05-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoportal', '0004_auto_20190522_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='geoportal.Tag'),
        ),
    ]

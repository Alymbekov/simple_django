# Generated by Django 2.2.1 on 2019-05-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoportal', '0003_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='posts',
            field=models.ManyToManyField(blank=True, to='geoportal.Post'),
        ),
    ]
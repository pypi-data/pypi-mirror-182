# Generated by Django 2.2.28 on 2022-10-31 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoldp_needle', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='tags',
            field=models.ManyToManyField(to='djangoldp_needle.Tag'),
        ),
    ]

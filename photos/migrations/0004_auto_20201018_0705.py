# Generated by Django 3.1.2 on 2020-10-18 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20201018_0421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='img',
        ),
    ]

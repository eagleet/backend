# Generated by Django 4.1.3 on 2022-11-08 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_registos_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registos',
            name='status',
        ),
    ]

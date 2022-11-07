# Generated by Django 4.1.3 on 2022-11-07 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_registosrespostas_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questoesregistos',
            name='tipoderegisto',
        ),
        migrations.AddField(
            model_name='questoesregistos',
            name='tipoderegisto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tiporegistos'),
        ),
    ]

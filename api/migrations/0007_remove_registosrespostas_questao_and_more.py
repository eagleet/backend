# Generated by Django 4.1.3 on 2022-11-07 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_questoesregistos_tipoderegisto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registosrespostas',
            name='questao',
        ),
        migrations.RemoveField(
            model_name='registosrespostas',
            name='registo',
        ),
        migrations.AddField(
            model_name='registosrespostas',
            name='questao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.questoesregistos'),
        ),
        migrations.AddField(
            model_name='registosrespostas',
            name='registo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.registos'),
        ),
    ]
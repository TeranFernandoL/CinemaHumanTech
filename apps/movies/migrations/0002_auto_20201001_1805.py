# Generated by Django 2.2.3 on 2020-10-01 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turn',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='turns',
            field=models.ManyToManyField(blank=True, null=True, to='movies.Turn', verbose_name='turnos'),
        ),
        migrations.AlterField(
            model_name='turn',
            name='schedule',
            field=models.TimeField(blank=True, null=True, unique=True, verbose_name='Horario'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-05 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuseradmin',
            name='is_istaff',
        ),
        migrations.AlterField(
            model_name='myuseradmin',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='Membro da equipe'),
        ),
    ]

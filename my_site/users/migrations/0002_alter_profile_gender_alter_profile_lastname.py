# Generated by Django 4.2.3 on 2023-07-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Мужчина', 'МУЖЧИНА'), ('Женщина', 'ЖЕНЩИНА')], default='Мужчина', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-18 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length_in_months', models.IntegerField()),
                ('from_friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_friends', to='users.profile')),
                ('to_friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='users.profile')),
            ],
        ),
    ]
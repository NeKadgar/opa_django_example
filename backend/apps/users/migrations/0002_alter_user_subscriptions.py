# Generated by Django 4.1.7 on 2023-03-29 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, related_name='users', to='users.subscription'),
        ),
    ]

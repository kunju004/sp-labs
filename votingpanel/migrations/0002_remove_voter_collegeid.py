# Generated by Django 3.1.5 on 2021-03-02 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votingpanel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='collegeid',
        ),
    ]
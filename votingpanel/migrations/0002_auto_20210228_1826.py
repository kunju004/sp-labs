# Generated by Django 3.1.5 on 2021-02-28 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votingpanel', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voters',
            new_name='Voter',
        ),
    ]
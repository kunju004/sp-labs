# Generated by Django 3.1.5 on 2021-03-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingpanel', '0007_auto_20210302_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='voting_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Voted', 'Voted')], max_length=10, null=True),
        ),
    ]
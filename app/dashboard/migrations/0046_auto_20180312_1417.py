# Generated by Django 2.0.3 on 2018-03-12 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0045_auto_20180228_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='standard_bounties_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
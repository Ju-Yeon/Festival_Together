# Generated by Django 2.1 on 2019-11-28 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20191128_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='usercount',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]

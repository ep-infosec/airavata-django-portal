# Generated by Django 3.2.11 on 2022-05-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_airavata_auth', '0015_auto_20220329_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduserprofilefield',
            name='required',
            field=models.BooleanField(default=True),
        ),
    ]

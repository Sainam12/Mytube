# Generated by Django 3.0.4 on 2020-03-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20200320_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accesspin',
            field=models.IntegerField(default=0),
        ),
    ]

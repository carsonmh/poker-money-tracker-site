# Generated by Django 4.0.6 on 2022-07-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_data', '0003_remove_moneylog_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneylog',
            name='money_info',
            field=models.TextField(default=''),
        ),
    ]

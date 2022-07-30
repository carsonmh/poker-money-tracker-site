# Generated by Django 4.0.6 on 2022-07-28 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('money_data', '0007_alter_moneylog_money_info_alter_moneylog_money_made'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneylog',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

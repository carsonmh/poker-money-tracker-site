# Generated by Django 4.0.6 on 2022-07-18 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_made', models.FloatField(help_text='test')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('info', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='MoneyAmount',
        ),
    ]

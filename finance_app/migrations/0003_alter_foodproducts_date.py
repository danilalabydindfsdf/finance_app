# Generated by Django 4.0.4 on 2022-04-19 11:38

from django.db import migrations, models
import finance_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0002_alter_foodproducts_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodproducts',
            name='date',
            field=models.DateTimeField(default=finance_app.models.get_time),
        ),
    ]
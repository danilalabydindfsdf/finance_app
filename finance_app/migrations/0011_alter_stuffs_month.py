# Generated by Django 4.0.4 on 2022-07-07 17:49

from django.db import migrations, models
import finance_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0010_ffoodproducts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuffs',
            name='month',
            field=models.TextField(default=finance_app.models.get_month),
        ),
    ]

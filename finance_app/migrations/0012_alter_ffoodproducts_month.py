# Generated by Django 4.0.4 on 2022-07-07 17:51

from django.db import migrations, models
import finance_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0011_alter_stuffs_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ffoodproducts',
            name='month',
            field=models.TextField(default=finance_app.models.get_month),
        ),
    ]
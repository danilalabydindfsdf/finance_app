# Generated by Django 4.0.4 on 2022-07-02 16:04

from django.db import migrations, models
import finance_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0009_sstuff'),
    ]

    operations = [
        migrations.CreateModel(
            name='FFoodProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(default=finance_app.models.get_time)),
                ('month', models.DateTimeField(default=finance_app.models.get_month)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]

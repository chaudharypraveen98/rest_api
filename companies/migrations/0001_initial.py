# Generated by Django 2.1.5 on 2019-12-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=10)),
                ('open_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('transaction', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('type_of_car', models.CharField(max_length=255)),
                ('volume', models.FloatField()),
            ],
        ),
    ]
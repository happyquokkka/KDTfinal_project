# Generated by Django 3.2.8 on 2021-11-05 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140, null=True)),
                ('upjong', models.CharField(max_length=30, null=True)),
                ('rating_average', models.DecimalField(decimal_places=2, max_digits=2, null=True)),
                ('address', models.CharField(max_length=140, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('rating_count', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('Latitude', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
                ('Longtitude', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
            ],
            options={
                'db_table': 'restaurant',
            },
        ),
    ]
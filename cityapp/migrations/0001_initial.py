# Generated by Django 2.0.6 on 2019-05-24 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pid', models.IntegerField(null=True)),
                ('cityname', models.CharField(max_length=255, null=True)),
                ('type', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'city',
                'managed': True,
            },
        ),
    ]

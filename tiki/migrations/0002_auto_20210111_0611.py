# Generated by Django 3.1.4 on 2021-01-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('url_path', models.CharField(max_length=200)),
                ('productset_group_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('list_price', models.IntegerField()),
                ('discount_rate', models.IntegerField()),
                ('rating_count', models.IntegerField()),
                ('rating_total', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='sell',
            options={'managed': False},
        ),
    ]

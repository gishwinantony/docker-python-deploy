# Generated by Django 5.0.7 on 2024-07-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_qty', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]

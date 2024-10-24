# Generated by Django 5.0.7 on 2024-10-01 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='categories/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('image', models.ImageField(default=None, max_length=250, null=True, upload_to='products/images/')),
                ('description', models.TextField()),
                ('stock', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminPanel.category')),
            ],
        ),
    ]

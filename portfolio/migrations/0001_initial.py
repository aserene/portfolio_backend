# Generated by Django 4.1.7 on 2023-03-12 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('tech', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]

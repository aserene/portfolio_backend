# Generated by Django 4.1.7 on 2023-03-31 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_item_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_item',
            name='github',
            field=models.CharField(default='https://github.com/aserene', max_length=100),
        ),
    ]

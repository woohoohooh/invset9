# Generated by Django 4.2.2 on 2023-06-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_product_productscore_rename_team_teamscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='asset_secured_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='emission_limit_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='liquidity_score',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-17 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_company_asset_secured_score_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productscore',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='securityscore',
            name='total_score',
        ),
        migrations.RemoveField(
            model_name='teamscore',
            name='total_score',
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-17 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_total_remove_emission_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productscore',
            name='name',
        ),
        migrations.RemoveField(
            model_name='securityscore',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teamscore',
            name='name',
        ),
        migrations.DeleteModel(
            name='Total',
        ),
    ]

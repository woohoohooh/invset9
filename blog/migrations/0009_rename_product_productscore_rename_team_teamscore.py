# Generated by Django 4.2.2 on 2023-06-17 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_product_name_team_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductScore',
        ),
        migrations.RenameModel(
            old_name='Team',
            new_name='TeamScore',
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-17 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_performace_product_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='securityscore',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
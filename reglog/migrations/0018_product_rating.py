# Generated by Django 3.1 on 2021-02-02 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglog', '0017_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

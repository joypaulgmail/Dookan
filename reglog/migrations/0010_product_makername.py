# Generated by Django 3.1 on 2020-12-27 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reglog', '0009_userdetails_itemadd'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='makername',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reglog.userdetails'),
        ),
    ]

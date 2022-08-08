# Generated by Django 4.0.6 on 2022-08-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
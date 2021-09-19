# Generated by Django 3.2.6 on 2021-09-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='day',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='home',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='night',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='outdoors',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=0, default='1', max_digits=6),
        ),
    ]

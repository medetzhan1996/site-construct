# Generated by Django 3.0.5 on 2020-07-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0007_auto_20200704_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_old',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]
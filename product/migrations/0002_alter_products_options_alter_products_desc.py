# Generated by Django 4.1 on 2022-09-03 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='products',
            name='desc',
            field=models.CharField(max_length=100),
        ),
    ]
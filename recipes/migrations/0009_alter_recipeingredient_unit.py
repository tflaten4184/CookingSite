# Generated by Django 4.2 on 2023-04-20 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_ingredient_base_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

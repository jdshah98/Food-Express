# Generated by Django 2.2.3 on 2019-08-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_food_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]

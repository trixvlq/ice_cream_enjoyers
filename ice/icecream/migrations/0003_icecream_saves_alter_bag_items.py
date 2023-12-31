# Generated by Django 4.2.7 on 2023-11-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0002_bag'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='saves',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bag',
            name='items',
            field=models.ManyToManyField(related_name='icecreams', to='icecream.icecream'),
        ),
    ]

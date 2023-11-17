# Generated by Django 4.2.7 on 2023-11-16 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icecream', '0003_icecream_saves_alter_bag_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0007_mincepierating'),
    ]

    operations = [
        migrations.AddField(
            model_name='mincepie',
            name='times_rated',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.2.5 on 2019-09-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='batch',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]

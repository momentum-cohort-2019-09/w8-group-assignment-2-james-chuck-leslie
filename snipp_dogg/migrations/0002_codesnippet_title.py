# Generated by Django 2.2.6 on 2019-10-31 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snipp_dogg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codesnippet',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

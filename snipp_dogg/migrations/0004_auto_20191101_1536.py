# Generated by Django 2.2.6 on 2019-11-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snipp_dogg', '0003_remove_codesnippet_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesnippet',
            name='language',
            field=models.CharField(choices=[('markup', 'markup'), ('css', 'css'), ('clike', 'clike'), ('javascript', 'javascript'), ('java', 'java'), ('json', 'json'), ('scss', 'scss'), ('python', 'python')], max_length=15),
        ),
    ]

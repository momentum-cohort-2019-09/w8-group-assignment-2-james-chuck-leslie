# Generated by Django 2.2.6 on 2019-10-29 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snipp_dogg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pinned_snippets',
            field=models.ManyToManyField(blank=True, related_name='user_pinned', to='snipp_dogg.CodeSnippet'),
        ),
        migrations.AlterField(
            model_name='codesnippet',
            name='language',
            field=models.CharField(default='python', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='codesnippet',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='derivatives', to='snipp_dogg.CodeSnippet'),
        ),
        migrations.AlterField(
            model_name='codesnippet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]

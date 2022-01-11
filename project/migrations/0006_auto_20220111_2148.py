# Generated by Django 3.2.11 on 2022-01-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_remove_project_link_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link_backtend',
        ),
        migrations.AddField(
            model_name='project',
            name='link_backend',
            field=models.URLField(blank=True, null=True),
        ),
    ]
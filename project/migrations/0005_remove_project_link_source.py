# Generated by Django 3.2.11 on 2022-01-11 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link_source',
        ),
    ]

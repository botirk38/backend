# Generated by Django 5.0 on 2023-12-29 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_boards', '0005_alter_task_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subtask',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]

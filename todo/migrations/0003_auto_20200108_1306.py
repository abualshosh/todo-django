# Generated by Django 2.2 on 2020-01-08 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='context',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='context', to='todo.Context'),
        ),
    ]

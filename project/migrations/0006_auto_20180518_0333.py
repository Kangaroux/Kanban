# Generated by Django 2.0.5 on 2018-05-18 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20180518_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='task',
            name='next_task',
        ),
        migrations.AddField(
            model_name='board',
            name='column_order',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='column',
            name='task_order',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='task',
            name='column',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='project.Column'),
            preserve_default=False,
        ),
    ]
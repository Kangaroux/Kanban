# Generated by Django 2.0.7 on 2018-07-23 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lib.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0007_auto_20180518_0400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(lib.models.Serializable, models.Model),
        ),
        migrations.RemoveField(
            model_name='board',
            name='owner',
        ),
        migrations.AddField(
            model_name='board',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
            preserve_default=False,
        ),
    ]
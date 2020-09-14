# Generated by Django 2.2.14 on 2020-09-14 04:59

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Silence',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', models.CharField(default='4c0b79cb98934625a775e4a327433949', max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('filter_args', django.contrib.postgres.fields.jsonb.JSONField(blank=True, verbose_name='沉默规则')),
                ('ignore_type', models.BooleanField(default=False, verbose_name='忽略类型')),
                ('duration', models.PositiveSmallIntegerField(default=60, verbose_name='沉默时间')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project', verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '- 沉默规则',
                'verbose_name_plural': '- 沉默规则',
            },
        ),
    ]

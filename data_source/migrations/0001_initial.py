# Generated by Django 2.2.14 on 2020-09-12 05:57

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_taggeduuiditem'),
        ('auth_token', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('草稿', '草稿'), ('发布', '发布'), ('下架', '下架')], default='草稿', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', models.CharField(default='4efa211312614110a054f9d88c4e3274', max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=50, verbose_name='数据源')),
                ('label', models.CharField(max_length=50, unique=True, verbose_name='标示符')),
                ('auto_close', models.BooleanField(default=True, verbose_name='自动关闭')),
                ('close_after', models.PositiveSmallIntegerField(default=360, verbose_name='关闭超时')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedUUIDItem', to='taggit.Tag', verbose_name='Tags')),
                ('tokens', models.ManyToManyField(blank=True, to='auth_token.AuthToken', verbose_name='认证令牌')),
            ],
            options={
                'verbose_name': '- 数据源管理',
                'verbose_name_plural': '- 数据源管理',
            },
        ),
    ]

from django.db import models
from message.constants import LEVEL_CHOICES, STATUS_CHOICES
from model_utils.models import TimeStampedModel
from utils.common.models import UUIDModel
from utils.taggit.models import TaggedUUIDItem
from taggit.managers import TaggableManager


# Create your models here.


class Message(UUIDModel, TimeStampedModel):
    project = models.CharField(verbose_name='项目标识', max_length=50)
    ds = models.CharField(verbose_name='数据源', max_length=50)
    type = models.CharField(verbose_name='消息标识', max_length=128)
    host = models.CharField(verbose_name='主机标识', max_length=128)
    title = models.CharField(verbose_name='消息标题', max_length=128)
    level = models.PositiveSmallIntegerField(verbose_name='消息等级', choices=LEVEL_CHOICES)
    status = models.PositiveSmallIntegerField(verbose_name='消息状态', choices=STATUS_CHOICES)
    raw = models.TextField(verbose_name='原始数据', blank=True, null=True)

    tags = TaggableManager(through=TaggedUUIDItem, blank=True)

    class Meta:
        verbose_name_plural = verbose_name = '- 消息管理'
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_project(self):
        from project.models import Project
        return Project.objects.get(label=self.project)

    def get_data_source(self):
        from data_source.models import DataSource
        return DataSource.objects.get(label=self.ds)

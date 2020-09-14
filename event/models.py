from django.db import models
from django.conf import settings
from utils.common.models import UUIDModel, OwnerModel, DateTimeFramedModel
from model_utils.models import TimeStampedModel, StatusModel, SoftDeletableModel
from model_utils.choices import Choices
from project.models import Project
from message.models import Message
from message.constants import LEVEL_CHOICES, LEVEL_WARNING
from event.constants import STATUS_CONVERGING, STATUS_RESOLVED, STATUS_REVOKED, STATUS_TIMEOUT
from converge.models import BurrConverge
from taggit.managers import TaggableManager
from utils.taggit.models import TaggedUUIDItem


# Create your models here.

class Event(UUIDModel, OwnerModel, DateTimeFramedModel, TimeStampedModel, StatusModel, SoftDeletableModel):
    """告警事件"""
    STATUS = Choices(STATUS_CONVERGING, STATUS_RESOLVED, STATUS_REVOKED, STATUS_TIMEOUT)
    name = models.CharField(verbose_name='事件名称', max_length=120)
    project = models.ForeignKey(Project, verbose_name='所属项目', on_delete=models.CASCADE)
    host = models.CharField(verbose_name='主机标识', max_length=128)
    level = models.PositiveSmallIntegerField(verbose_name='事件级别', choices=LEVEL_CHOICES, default=LEVEL_WARNING)
    grade = models.ForeignKey(Project, verbose_name='通知级别',
                              on_delete=models.CASCADE,
                              blank=True,
                              related_name='grade_events')
    messages = models.ManyToManyField(Message, verbose_name='关联消息')
    receivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       verbose_name='消息接收人',
                                       related_name='receive_events',
                                       blank=True)
    converge = models.ForeignKey(BurrConverge, verbose_name='毛刺收敛', on_delete=models.CASCADE)
    tags = TaggableManager(TaggedUUIDItem, blank=True)

    class Meta:
        verbose_name_plural = verbose_name = '- 告警事件'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        level = self.messages.order_by('-level').first().level
        self.level = level
        super(Event, self).save(*args, **kwargs)

from django.db import models
from utils.common.models import UUIDModel
from model_utils.models import StatusModel, TimeStampedModel, SoftDeletableModel
from model_utils.choices import Choices
from utils.common.constants import STATUS_PUBLISHED, STATUS_DRAFT, STATUS_OFFLINE
from auth_token.models import AuthToken
from taggit.managers import TaggableManager
from utils.taggit.models import TaggedUUIDItem


# Create your models here.


class DataSource(UUIDModel, StatusModel, TimeStampedModel, SoftDeletableModel):
    """数据源管理"""
    STATUS = Choices(STATUS_DRAFT, STATUS_PUBLISHED, STATUS_OFFLINE)
    name = models.CharField(verbose_name='数据源', max_length=50)
    label = models.CharField(verbose_name='标示符', max_length=50, unique=True)
    tokens = models.ManyToManyField(AuthToken, verbose_name='认证令牌', blank=True)
    auto_close = models.BooleanField(verbose_name='自动关闭', default=True)
    close_after = models.PositiveSmallIntegerField(verbose_name='关闭超时', default=360)

    tags = TaggableManager(through=TaggedUUIDItem, blank=True)

    class Meta:
        verbose_name_plural = verbose_name = '- 数据源管理'

    def __str__(self):
        return self.name

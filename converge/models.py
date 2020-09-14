from django.db import models
from utils.common.models import UUIDModel, OwnerModel, DateTimeFramedModel, TimeFramedModel
from model_utils.choices import Choices
from utils.common.constants import STATUS_PUBLISHED, STATUS_OFFLINE, STATUS_DRAFT
from model_utils.models import StatusModel, TimeStampedModel, SoftDeletableModel
from project.models import Project
from converge.constants import CONVERGE_REASON_CHOICES, SYSTEM_OPS


# Create your models here.


class BurrConverge(UUIDModel, OwnerModel, TimeStampedModel, SoftDeletableModel, StatusModel):
    """毛刺收敛: 基于多条件查询和匹配对应的消息"""
    STATUS = Choices(STATUS_DRAFT, STATUS_PUBLISHED, STATUS_OFFLINE)
    name = models.CharField(verbose_name='收敛规则', max_length=50)
    section = models.PositiveSmallIntegerField(verbose_name='收敛区间', default=5)
    count = models.PositiveSmallIntegerField(verbose_name='收敛阈值', default=3)
    project = models.ForeignKey(Project, verbose_name='收敛项目', on_delete=models.CASCADE)
    filter_args = models.TextField(verbose_name='过滤条件', blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '- 毛刺削峰收敛'

    def __str__(self):
        return self.name


class DateTimeConverge(UUIDModel, OwnerModel, TimeStampedModel, DateTimeFramedModel, SoftDeletableModel, StatusModel):
    """日期时间段收敛：某个时间段内的告警，收敛到一条，通知出来"""
    STATUS = Choices(STATUS_DRAFT, STATUS_PUBLISHED, STATUS_OFFLINE)
    name = models.CharField(verbose_name='收敛规则', max_length=50)
    reason = models.PositiveSmallIntegerField(verbose_name='收敛原因', choices=CONVERGE_REASON_CHOICES, default=SYSTEM_OPS)
    description = models.TextField(verbose_name=u'规则描述', blank=True, null=True)
    project = models.ForeignKey(Project, verbose_name='收敛项目', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = verbose_name = '- 日期时间收敛'

    def __str__(self):
        return self.name


class TimeConverge(UUIDModel, OwnerModel, TimeStampedModel, TimeFramedModel, SoftDeletableModel, StatusModel):
    """每天固定时间段收敛: 每天固定时间段内的告警进行收敛"""
    STATUS = Choices(STATUS_DRAFT, STATUS_PUBLISHED, STATUS_OFFLINE)

    class Meta:
        verbose_name_plural = verbose_name = '- 固定时间收敛'

    def __str__(self):
        return self.owner.username

from uuid import uuid4
from django.db import models
from utils.common.models import UUIDModel, OwnerModel
from model_utils.models import TimeFramedModel, StatusModel
from model_utils.choices import Choices
from utils.common.constants import STATUS_PUBLISHED, STATUS_DRAFT, STATUS_OFFLINE
from datetime import datetime


# Create your models here.


class AuthToken(UUIDModel, OwnerModel, StatusModel, TimeFramedModel):
    """仿照 rest_framework.authtoken 自定义 token """
    STATUS = Choices(STATUS_DRAFT, STATUS_PUBLISHED, STATUS_OFFLINE)

    name = models.CharField(verbose_name='秘钥名称', max_length=50)
    token = models.CharField(verbose_name='认证秘钥', max_length=32, default=uuid4().hex)

    class Meta:
        verbose_name_plural = verbose_name = '- 密钥认证'
        ordering = ['owner__username']

    @property
    def is_expired(self) -> str:
        """
        检测 token 是否过期
        @return: bool
        """
        start = self.start or datetime.now()
        end = self.end or datetime.now()

        if start <= datetime.now() <= end:
            return '未过期'
        return '已过期'

    @property
    def is_enabled(self) -> bool:
        """
        是否启用 token
        @return: bool
        """
        if self.status is STATUS_PUBLISHED:
            return True
        return False

    def __str__(self):
        return "%s_%s" % (self.owner, self.name)

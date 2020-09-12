from uuid import uuid4
from django.db import models
from utils.common.models import UUIDModel, OwnerModel, DateTimeFramedModel
from model_utils.models import StatusModel, SoftDeletableModel
from model_utils.choices import Choices
from utils.common.constants import STATUS_PUBLISHED, STATUS_DRAFT, STATUS_OFFLINE


# Create your models here.


class AuthToken(UUIDModel, OwnerModel, StatusModel, DateTimeFramedModel, SoftDeletableModel):
    """仿照 rest_framework.authtoken 自定义 token """
    STATUS = Choices(STATUS_DRAFT, STATUS_PUBLISHED, STATUS_OFFLINE)

    name = models.CharField(verbose_name='秘钥名称', max_length=50)
    token = models.CharField(verbose_name='认证秘钥', max_length=32, default=uuid4().hex)

    class Meta:
        verbose_name_plural = verbose_name = '- 密钥认证'
        ordering = ['owner__username']

    def __str__(self):
        return "%s_%s" % (self.owner, self.name)

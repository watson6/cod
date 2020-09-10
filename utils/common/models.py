"""自定义通用模型字段"""
from uuid import uuid4
from django.db import models
from django.conf import settings


class UUIDModel(models.Model):
    """uuid"""
    id = models.CharField(verbose_name='id', max_length=32, default=uuid4().hex, primary_key=True, unique=True)

    class Meta:
        abstract = True


class OwnerModel(models.Model):
    """用户模型虚类"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        abstract = True

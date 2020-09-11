import logging
from celery import shared_task

logger = logging.getLogger('root')


@shared_task(ignore_result=True)
def message_handler(message_id):
    """
    告警消息异步处理：告警收敛
    :param message_id: Message Object Id
    """
    print(message_id)

import time
import uuid
import requests
import json
from datetime import datetime
from random import randint
from django.core.management.base import BaseCommand

ALERTS = [
    {
        "project": "devops",
        "message": "host.cpu.everage10",
        "host": "www.126.com",
        "title": "CPU everage5",
        "level": 1,
        "status": 0,
    },
    {
        "project": "devops",
        "message": "host.cpu.everage5",
        "host": "www.baidu.com",
        "title": "CPU 过高",
        "level": 1,
        "status": 0,
    },
    {
        "project": "devops",
        "message": "host.cpu.everage5",
        "host": "www.baidu.com",
        "title": "CPU 过高",
        "level": 1,
        "status": 1,
    }
]


class Command(BaseCommand):
    help = 'produce message and post to local message api'

    API = 'http://dev.cod.com:8000/message/receiver/'
    HEADERS = {
        "Authorization": "token 702e6b5e-59b8-431a-b952-06c6cf22a480"
    }

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, help='count of alerts to produce')

    def handle(self, *args, **options):
        count = options['count']
        if count:
            self.limit_producer(count=count)
        else:
            self.unlimit_producer()

    def limit_producer(self, count):
        """
        :param count: count of alerts to produce
        """
        for _ in range(count):
            # time.sleep(1)
            self.producer()

    def unlimit_producer(self):
        while True:
            # time.sleep(1)
            self.producer()

    def producer(self):
        data = self.random_alert()
        data.update({"trace": str(uuid.uuid4()), "time": datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')})
        # with open('alerts.txt', 'a+') as f:
        #     f.write(json.dumps(data)+','+'\n')
        #     self.stdout.write(json.dumps(data))
        response = requests.request("POST", self.API, headers=self.HEADERS, data=data)
        self.stdout.write(msg=response.text)

    @staticmethod
    def random_alert():
        random = randint(0, len(ALERTS) - 1)
        return ALERTS[random]

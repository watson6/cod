import json
import requests
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'prometheus alertmanager trigger'
    API = 'http://dev.cod.com:9093/api/v1/alerts/'

    def handle(self, *args, **options):
        headers = {
            'Content-Type': 'application/json'
        }

        payload = [
            {
                "labels": {
                    "alertname": "alertname",
                    "severity": "warning",
                    "ipaddress": "127.10.20.30"
                },
                "annotations": {
                    "description": "Instance play-app:9000 under lower load",
                    "summary": "play-app:9000 of job play framework app is under lower load"
                }
            },
            {
                "labels": {
                    "alertname": "alertname",
                    "severity": "critical",
                    "ipaddress": "8.8.8.8"
                },
                "annotations": {
                    "description": "Instance play-app:9000 under lower load",
                    "summary": "play-app:9000 of job play framework app is under lower load"
                }
            }
        ]
        response = requests.request("POST", self.API, headers=headers, data=json.dumps(payload))
        self.stdout.write(response.text + "\n")

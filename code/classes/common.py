"""
    Common methods used by all modules from app.
"""
import json
from .configuration import CONFIGURATION_FILE

def __get_webhook_informations__(service, room):
        with open(CONFIGURATION_FILE, 'r') as config_file:
            webhooks = json.loads(config_file.read())

            for webhook in webhooks['webhooks_room']:
                if webhook['name'] == str(room) and webhook['service'] == service:
                    return webhook

def __message_send__(response_result):
        if response_result[0]['status'] == 200:
            return True
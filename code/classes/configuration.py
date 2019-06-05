"""
    Module to configure the app
"""
from .version import APP_NAME
import os

HOME = os.environ['HOME']
CONFIGURATION_DIR = f"{HOME}/.{APP_NAME}/config"
CONFIGURATION_FILE = f"{CONFIGURATION_DIR}/webhooks.json"

CONFIGURATION_FILE_TEMPLATE = """
{
    "webhooks_room": [
        {
            "service": "google",
            "name": "room_name",
            "bot_name": "bot_name",
            "url": "https://chat.googleapis.com/"
        },
        {
            "service": "slack",
            "name": "room_name",
            "bot_name": "bot_name",
            "url": "https://teste.slack.com/"
        }
    ]
}
"""

class Configuration():

    @staticmethod
    def create_configurations():
        if not os.path.exists(CONFIGURATION_DIR):
            os.makedirs(CONFIGURATION_DIR)

            if not os.path.exists(CONFIGURATION_FILE):
                with open(CONFIGURATION_FILE, 'a') as config_file:
                    config_file.write(CONFIGURATION_FILE_TEMPLATE)
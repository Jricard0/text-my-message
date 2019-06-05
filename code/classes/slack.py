"""
    Module to send messages on slack
"""
from termcolor import colored
from httplib2 import Http
from json import dumps
from .common import __get_webhook_informations__, __message_send__

class Slack():
    def __init__(self, room, text, icon):
        self.room = room
        self.text = text
        self.icon = icon

    def perform(self):
        hook = __get_webhook_informations__(service='slack', room=self.room)
        __message_send__(response_result=self.create_message(webhook=hook))

    def create_message(self, webhook):
        if not webhook:
            print(colored("ERROR:", color='red'), f"No configuration provided for room ~> {self.room}")
            exit(3)

        url = webhook['url']

        bot_message = {
            'channel': str(self.room),
            'username': str(webhook['bot_name']),
            'text': str(self.text),
            'icon_emoji': f":{self.icon}:"
        }

        message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

        http_obj = Http()

        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )

        return response
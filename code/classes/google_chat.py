"""
    Module to send messages by chat google
"""

from httplib2 import Http
from json import dumps
import os
import json
from termcolor import colored
from classes.configuration import CONFIGURATION_FILE
from classes.common import __get_webhook_informations__, __message_send__

class GoogleChat():
    def __init__(self, room, text):
        self.room = room
        self.text = text

    def perform(self):
        hook = __get_webhook_informations__(service='google', room=self.room)
        __message_send__(response_result=self.create_message(message=str(self.text), webhook=hook))

    def create_message(self, message, webhook):

        if not webhook:
            print(colored("ERROR:", color='red'), f"No configuration provided for room ~> {self.room}")
            exit(3)

        url = webhook['url']
        bot_message = {
            'text' : str(message)
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
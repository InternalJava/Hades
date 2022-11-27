#from discordWebhook import Webhook
from os import system as _sys
import random

class Log():
    def _sendWebhook(url : str, message : str):
        #logs = Webhook.Create(url)
        #logs.send(message)
        print("[LOGS]: '{0}'".format(message))
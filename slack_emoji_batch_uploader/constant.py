import os
from dotenv import load_dotenv
load_dotenv()
try:
     cookies = {
          'd': os.environ['COOKIE_D'],
     }
     WORKSPACE = os.environ['WORKSPACE']
     token = os.environ['TOKEN']
except KeyError as ex:
     raise KeyError(f"Please remember set .env file, env:{ex} not set")
slack_add = f'https://{WORKSPACE}.slack.com/api/emoji.add'
slack_delete = f'https://{WORKSPACE}.slack.com/api/emoji.remove'
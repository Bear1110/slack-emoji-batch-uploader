import requests
from slack_emoji_batch_uploader.constant import cookies, token, slack_delete

def delete_emoji(emoji_name):
    payload = {
        'token': token,
        'name': emoji_name,
        '_x_reason': 'customize-emoji-remove',
        '_x_mode': 'online'
      }
    res = requests.request("POST", slack_delete, cookies=cookies, data=payload, files=[])
    response_json = res.json()
    if not response_json['ok']:
        print(emoji_name, response_json)
    return response_json['ok']
    
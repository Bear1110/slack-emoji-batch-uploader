'''Provide a func call slack delete api'''
import requests
from slack_emoji_batch_uploader.constant import cookies, token, slack_delete

def delete_emoji(emoji_name):
    '''
    Delete a emoji by emoji_name (emoji tag)
    '''
    payload = {
        'token': token,
        'name': emoji_name,
        '_x_reason': 'customize-emoji-remove',
        '_x_mode': 'online'
      }
    res = requests.request(
        "POST",
        slack_delete,
        cookies=cookies,
        data=payload,
        files=[],
        timeout=60
    )
    response_json = res.json()
    if not response_json['ok']:
        print(emoji_name, response_json)
    return response_json['ok']

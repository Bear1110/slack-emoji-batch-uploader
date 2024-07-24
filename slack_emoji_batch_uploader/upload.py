import requests
from slack_emoji_batch_uploader.constant import slack_add, cookies, token


def upload_emoji(emoji_name, file_path):
    files=[
        (
            'image',
            ('not important.png',open(file_path,'rb'),'image/png')
        )
    ]
    payload = {
        'token': token,
        'name': emoji_name,
        'mode': 'data',
        'search_args': '{"sort_by":"created","sort_dir":"desc"}',
        '_x_reason': 'add-custom-emoji-dialog-content',
        '_x_mode': 'online'
    }
    res = requests.post(
        slack_add,
        cookies=cookies,
        data=payload,
        files=files,
        timeout=60,
    )
    response_json = res.json()
    if not response_json['ok']:
        print(file_path, emoji_name, response_json)
    return response_json['ok']

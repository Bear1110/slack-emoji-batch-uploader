'''Module providing a function for upload emoji in a folder'''
import argparse

from slack_emoji_batch_uploader.upload import upload_emoji
from slack_emoji_batch_uploader.utils import get_filename, is_folder_exist, get_image_files


def upload_emoji_in_folder(folder):
    '''
    Upload all emoji in a folder
    '''
    onlyfiles = get_image_files(folder)
    for i, file_path in enumerate(onlyfiles):
        emoji_name = get_filename(file_path)
        if upload_emoji(emoji_name, file_path):
            print(f'upload [{emoji_name}], {file_path}, {i + 1}/{len(onlyfiles)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder",
                        help="the folder of emoji you want to upload",
                        type=is_folder_exist, default="./tiles")
    args = parser.parse_args()

    upload_emoji_in_folder(args.folder)

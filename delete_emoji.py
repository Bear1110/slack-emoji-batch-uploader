import argparse

from os import listdir
from os.path import isfile, join
from slack_emoji_batch_uploader.delete import delete_emoji
from slack_emoji_batch_uploader.utils import get_extention, get_filename, is_folder_exist

files_extensions = set(['png', 'jpg', 'jpeg'])


def main(folder):
    onlyfiles = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]
    for i, file_path in enumerate(onlyfiles):
        if get_extention(file_path) not in files_extensions:
            print(f'skip {file_path}, not in files_extensions')
            continue
        emoji_name = get_filename(file_path)
        if delete_emoji(emoji_name):
            print(f'delete [{emoji_name}] {i + 1}/{len(onlyfiles)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", help="the folder of emoji you want to delete", type=is_folder_exist, default="./tiles")
    args = parser.parse_args()

    main(args.folder)
import argparse

from os import listdir
from os.path import isfile, join, basename, isdir
from slack_emoji_batch_uploader.upload import upload_emoji

files_extensions = set(['png', 'jpg', 'jpeg'])

def get_extention(file_path):
    return file_path.split('.')[-1]

def get_filename(file_path):
    return basename(file_path).split('.')[0]


def main(folder):
    onlyfiles = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]
    for i, file_path in enumerate(onlyfiles):
        if get_extention(file_path) not in files_extensions:
            print(f'skip {file_path}, not in files_extensions')
            continue
        emoji_name = get_filename(file_path)
        if upload_emoji(emoji_name, file_path):
            print(f'upload [{emoji_name}], {file_path}, {i + 1}/{len(onlyfiles)}')

def is_folder_exist(path):
    assert isdir(path), f'[{path}] is not a folder, either not exist in your machine'
    return path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", help="the folder of emoji you want to upload", type=is_folder_exist, default="./tiles")
    args = parser.parse_args()

    main(args.folder)
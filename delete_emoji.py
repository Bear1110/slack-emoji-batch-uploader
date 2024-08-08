"""Module providing a function for delete emoji in a folder"""

import argparse

from slack_emoji_batch_uploader.delete import delete_emoji
from slack_emoji_batch_uploader.utils import (
    get_filename,
    is_folder_exist,
    get_image_files,
)


def delete_emoji_in_folder(folder):
    """
    delete multiple emoji in a folder
    """
    onlyfiles = get_image_files(folder)
    for i, file_path in enumerate(onlyfiles):
        emoji_name = get_filename(file_path)
        if delete_emoji(emoji_name):
            print(f"delete [{emoji_name}] {i + 1}/{len(onlyfiles)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--folder",
        help="the folder of emoji you want to delete",
        type=is_folder_exist,
        default="./tiles",
    )
    args = parser.parse_args()

    delete_emoji_in_folder(args.folder)

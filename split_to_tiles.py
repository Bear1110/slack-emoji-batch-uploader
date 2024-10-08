import argparse

from slack_emoji_batch_uploader.split_image import split_image
from slack_emoji_batch_uploader.split_image_gif import split_gif
from slack_emoji_batch_uploader.utils import is_file_exist

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="the image you want to split", type=is_file_exist)
    parser.add_argument("emoji_name", help="the emoji prefix", type=str)
    parser.add_argument(
        "-w", "--width", help="the width of square", type=int, default=128
    )
    parser.add_argument(
        "-o", "--output_dir", help="output dir", type=str, default="./tiles"
    )
    parser.add_argument(
        "-g",
        "--gif",
        help="is image a gif",
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
    )
    args = parser.parse_args()

    if not args.gif:
        split_image(args.file, args.emoji_name, args.width, args.output_dir)
    else:
        split_gif(args.file, args.emoji_name, args.width, args.output_dir)

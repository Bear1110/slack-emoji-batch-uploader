"""Provide a func for split image"""

import os

from PIL import Image

from .utils import write_txt_file


def _save_tile(tile, filename, output_dir):
    tile_path = os.path.join(output_dir, f"{filename}.png")
    tile.save(tile_path)


def split_image(file_path, emoji_name, square_width, output_dir):
    """
    Give a file_path, split it by square_width
    Named tiled by emoji_name and saved it to output_dir.
    """
    image = Image.open(file_path)
    img_width, img_height = image.size
    os.makedirs(output_dir, exist_ok=True)

    tile_number = 0
    emoji_text = []
    for y in range(0, img_height, square_width):
        row_text = []
        for x in range(0, img_width, square_width):
            # calc square coordinate
            box = (x, y, x + square_width, y + square_width)
            # crop image to tile
            tile = image.crop(box)
            filename = f"{emoji_name}_{y // square_width}_{x // square_width}"
            _save_tile(tile, filename, output_dir)
            row_text.append(f":{filename}:")
            tile_number += 1
        emoji_text.append(row_text)
    write_txt_file(emoji_text, emoji_name, output_dir)
    print(f"successfully split [{file_path}] to {tile_number} tiles in {output_dir}")

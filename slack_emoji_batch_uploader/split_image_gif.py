import os
from collections import defaultdict

from PIL import Image, ImageSequence

from .utils import write_txt_file


def _generate_emoji_text(height, width, square_width, emoji_name):
    emoji_text = []

    for y in range(0, height, square_width):
        row = []
        for x in range(0, width, square_width):
            row.append(f":{emoji_name}_{y//square_width}_{x//square_width}:")
        emoji_text.append(row)
    return emoji_text


def split_gif(file_path, emoji_name, square_width, output_dir):
    """
    Give a file_path, split it by square_width
    Named tiled by emoji_name and saved it to output_dir.
    """
    image = Image.open(file_path)
    img_width, img_height = image.size
    os.makedirs(output_dir, exist_ok=True)

    gif_path = file_path
    gif = Image.open(gif_path)
    img_width, img_height = gif.size
    tiles = defaultdict(list)
    for frame_number, frame in enumerate(ImageSequence.Iterator(gif)):
        frame = frame.convert("RGBA")
        for y in range(0, img_height, square_width):
            for x in range(0, img_width, square_width):
                box = (x, y, x + square_width, y + square_width)
                tile = frame.crop(box)
                tile_key = (y, x)
                tiles[tile_key].append(tile)

    for tile_key, frames in tiles.items():
        y, x = tile_key
        filename = f"{emoji_name}_{y//square_width}_{x//square_width}.gif"
        tile_path = os.path.join(output_dir, filename)
        frames = []
        for frame in frames:
            frames.append(frame)
        frames[0].save(
            tile_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            optimize=True,
        )
    emoji_text = _generate_emoji_text(img_height, img_width, square_width, emoji_name)
    write_txt_file(emoji_text, emoji_name, output_dir)
    print(f"successfully split [{file_path}] tiles in {output_dir}")

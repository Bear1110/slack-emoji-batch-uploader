import os
from PIL import Image


def _save_tile(tile, filename, output_dir):
    tile_path = os.path.join(output_dir, f'{filename}.png')
    tile.save(tile_path)

def _write_txt_file(emoji_text, emoji_name, output_dir):
    tile_path = os.path.join(output_dir, f"{emoji_name}.txt")
    with open(tile_path, "w") as text_file:
        s = '\n'.join([''.join(row) for row in emoji_text])
        text_file.write(s)


def split_image(file_path, emoji_name, square_width, output_dir):
    image = Image.open(file_path)
    img_width, img_height = image.size
    os.makedirs(output_dir, exist_ok=True)

    tile_number = 0
    x_index, y_index = 0, 0
    emoji_text = []
    for y in range(0, img_height, square_width):
        row_text = []
        for x in range(0, img_width, square_width):
            # calc square coordinate
            box = (x, y, x + square_width, y + square_width)
            # crop image to tile
            tile = image.crop(box)
            filename = f'{emoji_name}_{y_index}_{x_index}'
            _save_tile(tile, filename, output_dir)
            row_text.append(f':{filename}:')
            tile_number += 1
            x_index += 1
        emoji_text.append(row_text)
        x_index = 0
        y_index += 1
    _write_txt_file(emoji_text, emoji_name, output_dir)
    print(f'successfully split [{file_path}] to {tile_number} tiles in {output_dir}')

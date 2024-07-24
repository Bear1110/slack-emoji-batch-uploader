# slack-emoji-batch-uploader
This tool provides the following functionalities:

1. Split a large image into multiple tiles to assist users in uploading them as Slack emojis. (`split_to_tiles.py`)
2. Read a folder and batch upload the images as emojis to Slack. (`upload_emoji.py`)
3. Delete emojis from Slack based on filenames in a folder. (`delete_emoji.py`)

## Installation
### poetry
```
poetry shell
```
### pip
```
pip install -r requirement.txt
```

## Prerequisites authication
To use this tool, you need to set up the following environment variables. You can refer to the `.env.example` file provided in the repository for guidance.

- COOKIE_D=example
- WORKSPACE=example
- TOKEN=example

You can either copy `.env.example` to `.env` and modify the values, or set these variables directly in your environment.

```
cp .env.example .env
# Then edit the .env file to include your actual values
```

You could read this [docs](docs/README.md) to get `COOKIE_D` and `TOKEN`.


`WORKSPACE` is the slack workspace, something like this -> https://{{WORKSPACE}}.slack.com/customize/emoji


## Usage

### Batch upload emoji
This script, upload_emoji.py, is designed to upload emojis from a specified folder. The folder containing the emojis can be provided as an argument when running the script. If no folder is specified, the script will default to the `./tiles` folder.

It use filename as emoji tag name, e.g. filename: **abc_5_4.png** -> emoji tag: **:abc_5_4:**
#### Example Usage
```
python upload_emoji.py -f /path/to/emoji/folder
```

### Split image to tiles
This feature allows users to divide a large image into smaller tiles, making it easier to upload them as individual emojis to Slack.

Also, it generate a **emoji.txt** for user easily paste to **reconstruct** the image in slack app.

#### Example Usage
```
python split_to_tiles.py path/to/your/image.png emoji_prefix -w 128 -o ./tiles
```

### Batch Delete  emoji
This feature allows users to delete emoji from a specified folder.

#### Example Usage
```
python delete_emoji.py -f /path/to/emoji/folder
```


## License
This project is licensed under the MIT License. See the LICENSE file for more details.
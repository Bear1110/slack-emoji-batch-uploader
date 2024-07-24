from os.path import basename, isdir, isfile

def get_extention(file_path):
    return file_path.split('.')[-1]

def get_filename(file_path):
    return basename(file_path).split('.')[0]

def is_folder_exist(path):
    assert isdir(path), f'[{path}] is not a folder, either not exist in your machine'
    return path

def is_file_exist(path):
    assert isfile(path), f'[{path}] is not exist in your machine'
    return path

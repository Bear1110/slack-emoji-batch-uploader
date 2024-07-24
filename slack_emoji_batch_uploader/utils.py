'''Provide some utils func, like file operation'''
from os import listdir
from os.path import isfile, join, basename, isdir

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

def get_image_files(folder):
    files_extensions = set(['png', 'jpg', 'jpeg'])
    onlyfiles = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f))]
    return [file_path for file_path in onlyfiles if get_extention(file_path) in files_extensions]

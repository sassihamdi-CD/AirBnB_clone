#!/usr/bin/python3
'''this contain tests for the AirBnb clone modules.
'''
import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO):
    ''' the method that clears the contents of a given stream

    Arguments:
        stream (TextIO): The stream to clear.
    '''
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)


def delete_file(file_path: str):
    ''' the method that removes a file if it exists.
    Arguments:
        file_path (str): The name of the file to remove.
    '''
    if os.path.isfile(file_path):
        os.unlink(file_path)


def reset_store(store: FileStorage, file_path='file.json'):
    '''the method that resets the items in the given store.
    Arguments:
        store (FileStorage): The FileStorage to reset.
        file_path (str): The path to the store's file.
    '''
    with open(file_path, mode='w') as file:
        file.write('{}')
    if store is not None:
        store.reload()


def read_text_file(file_name):
    '''the method that reads the contents of a given file.

    Arguments:
        file_name (str): The name of the file to read.

    Returns:
        str: The contents of the file if it exists.
    '''
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)


def write_text_file(file_name, text):
    '''the method that writes a text to a given file.

    Arguments:
        file_name (str): The name of the file to write to.
        text (str): The content of the file.
    '''
    with open(file_name, mode='w') as file:
        file.write(text)

import os
from time import time


def _fish_history_file_location():
    possible_paths = [
        os.path.join(os.environ["HOME"], ".local/share/fish/fish_history"),
        os.path.join(os.environ["HOME"], ".config/fish/fish_history"),
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None


def fish_history_file_lines():
    history_file = _fish_history_file_location()
    if history_file is None:
        return []
    with open(history_file, 'r') as history:
        lines = history.readlines()
        return lines


def _zsh_history_file_location():
    possible_paths = [
        os.path.join(os.environ["HOME"], ".zsh_history"),
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None


def zsh_history_file_lines():
    history_file = _zsh_history_file_location()
    if history_file is None:
        return []
    with open(history_file, 'r') as history:
        lines = history.read().splitlines()
        return lines


def _get_history_line(command_script):
    return u'- cmd: {}\n  when: {}\n'.format(command_script, int(time()))


def save(cmd):
    history_file = _fish_history_file_location()
    if os.path.isfile(history_file):
        with open(history_file, 'a') as history:
            entry = _get_history_line(cmd)
            history.write(entry)

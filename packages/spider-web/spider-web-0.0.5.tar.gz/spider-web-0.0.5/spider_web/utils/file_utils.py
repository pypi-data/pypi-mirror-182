"""
Utilities module for file operations #

:author: Julian M. Kleber
"""

import os
import logging


def norm_path(path):
    """Convert slashes and backward slashes depending on operating system"""

    path = path.replace("\\", os.path.sep)

    return path


def check_make_dir(dir_name: str):
    """
    The check_make_dir function checks if a directory exists. If it does not exist, the function creates it.

    :param dir_name:str: Used to Specify the folder name.
    :return: None.

    :doc-author: Trelent
    """

    # You should change 'test' to your preferred folder.
    check_folder = os.path.isdir(dir_name)
    logging.info("Checked the directory " + str(dir_name))
    # If folder doesn't exist, then create it.
    if not check_folder:
        os.makedirs(dir_name)
        logging.info("created folder : " + str(dir_name))

    else:
        logging.info(dir_name + "folder already exists.")

"""
Module to se the netstat functionality outside of a CLI application. 

:author: Julian M. Kleber
"""
from datetime import datetime
from spider_web.utils.file_utils import check_make_dir, norm_path
import click
from spider_web.record_netstat import run_netstat


def record_netstat(o: str):
    """
    The record_netstat function records the output of netstat -an to a file.
        The filename is formatted as YYYY-MM-DD_HH:MM, where YYYY is the year, MM is the month, DD is the day of
        month and HH:MM are hours and minutes respectively.

    :return: A file with the output of the netstat -an command.

    :doc-author: Julian M. Kleber
    """
    run_netstat(out_dir=o)


if __name__ == "__main__":
    record_netstat(r"U:/")

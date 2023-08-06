import subprocess
from datetime import datetime
from spider_web.utils.file_utils import check_make_dir, norm_path
import click
import time


@click.command()
@click.option("-o", help="ouput file")
@click.option("-t", default=60, help="time interval in seconds")
def record_netstat(o: str, t: int | float):
    """
    The record_netstat function records the output of netstat -an to a file.
        The filename is formatted as YYYY-MM-DD_HH:MM, where YYYY is the year, MM is the month, DD is the day of
        month and HH:MM are hours and minutes respectively.

    :return: A file with the output of the netstat -an command.

    :doc-author: Julian M. Kleber
    """
    if o is None:
        raise TypeError(
            "Please specify the output directory using the -o option")
    if o == ".":
        o = "./"

    while True:
        run_netstat(out_dir=o)
        time.sleep(t)


def run_netstat(out_dir: str):

    out_dir = norm_path(out_dir)
    check_make_dir(out_dir)
    t = datetime.now()
    format1 = r"%Y-%m-%d-%H%M%S"
    t = datetime.strftime(t, format1)
    with open(out_dir + t + "_netstat.txt", "w") as f:
        subprocess.run(["netstat", "-tape"], stdout=f)


if __name__ == "__main__":
    record_netstat()

from pathlib import Path
from time import time
from typing import Callable
# noinspection PyUnresolvedReferences
import docx2pdf, PyPDF2

SOURCE = Path("../source")
OUT = Path("../out")


def clean_up():
    for i in OUT.iterdir():
        i.unlink()
    print("cleaned files up")


def time_it(func: Callable):
    # clean_up()
    start = time()
    func()
    print(time()-start)


if __name__ == '__main__':
    clean_up(print)

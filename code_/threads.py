import docx2pdf

from interface import *
import threading
import pythoncom


def conv(in_: Path, out_: Path):
    pythoncom.CoInitialize()
    docx2pdf.convert(input_path=in_, output_path=out_)


@time_it
def main():
    threads = []
    for file in SOURCE.iterdir():
        thread = threading.Thread(target=conv,
                                  args=(file, OUT / f"{file.stem}.pdf"))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    try:
        main() #27sec
    except TypeError:
        print("...")

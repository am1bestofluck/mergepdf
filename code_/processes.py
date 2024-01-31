import multiprocessing

from interface import docx2pdf, Path, SOURCE, OUT, clean_up, time


# from threads import conv


def conv(in_: Path, out_: Path):
    docx2pdf.convert(input_path=in_, output_path=out_)


if __name__ == '__main__':
    start = time()
    clean_up()
    multiprocessing.freeze_support()
    processes = []
    for file in SOURCE.iterdir():
        prc = multiprocessing.Process(target=conv, args=(file,
                                                         OUT / f"{file.stem}.pdf"))
        processes.append(prc)
        prc.start()
    for process in processes:
        process.join()
    print(time()-start) #31


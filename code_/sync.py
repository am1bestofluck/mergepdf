from interface import *


@time_it
def main():
    for file in SOURCE.iterdir():
        docx2pdf.convert(file, OUT / f"{file.stem}.pdf")


if __name__ == '__main__':
    try:
        clean_up()
        main() # 40 sec
    except TypeError:
        print("...")

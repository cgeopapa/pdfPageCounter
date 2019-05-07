import sys
from os import listdir
from os.path import isfile, join, exists

import PyPDF2


def getFileList(path):
    pdfList = [join(path, f) for f in listdir(path) if (isfile(join(path, f)) and f.endswith(".pdf"))]
    return pdfList


def pageCounter(pdfList):
    count = 0
    for pdfPath in pdfList:
        pdf = PyPDF2.PdfFileReader(open(pdfPath, "rb"))

        if pdf.flattenedPages is None:
            count += pdf.getNumPages()
    return count


if __name__ == "__main__":
    path = sys.argv[1]
    if exists(path):
        pdfList = getFileList(path)
        print(pageCounter(pdfList))
    else:
        print("No such directory exists")
        exit(0)

#! /usr/local/bin/python3.7

from PyPDF2 import PdfFileReader
import argparse


def printMetaData(pdfFile):
    with open(pdfFile, "rb") as f:
        pdf = PdfFileReader(f)
        docInfo = pdf.getDocumentInfo()
    print("metadata for {0}".format(pdfFile))
    for metaItem in docInfo:
        print("metaitem {0}: {1}".format(metaItem, docInfo[metaItem]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    printMetaData(args.filename)


if __name__ == "__main__":
    main()

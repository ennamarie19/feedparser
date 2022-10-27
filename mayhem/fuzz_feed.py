#! /usr/bin/python3
import tempfile

import atheris
import sys
import io

with atheris.instrument_imports():
    import feedparser

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    file_data = fdp.ConsumeBytes(atheris.ALL_REMAINING)
    temp_file = tempfile.NamedTemporaryFile()
    temp_file.write(file_data)
    temp_file.flush()
    feedparser.parse(temp_file.name)


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()

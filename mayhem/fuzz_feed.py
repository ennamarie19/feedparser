#! /usr/bin/python3
import tempfile

import atheris
import sys
import io
import random

with atheris.instrument_imports():
    import feedparser

def TestOneInput(data):
    try:
        fdp = atheris.FuzzedDataProvider(data)
        file_data = fdp.ConsumeUnicodeNoSurrogates(atheris.ALL_REMAINING)
        f = io.StringIO(file_data)
        #temp_file = tempfile.NamedTemporaryFile()
        #temp_file.write(file_data)
        #temp_file.flush()
        feedparser.parse(f)

    except IndexError:
        if random.randint(0, 100) == 50:
            raise

    #temp_file.close()

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()

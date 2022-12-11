#!/usr/bin/env python3
import tempfile

import atheris
import sys
import io
import random

with atheris.instrument_imports(include=['feedparser']):
    import feedparser

def TestOneInput(data):
    try:
        fdp = atheris.FuzzedDataProvider(data)
        file_data = fdp.ConsumeUnicodeNoSurrogates(atheris.ALL_REMAINING)
        feedparser.parse(file_data)

    except IndexError:
        if random.randint(0, 100) == 50:
            raise

    #temp_file.close()

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()

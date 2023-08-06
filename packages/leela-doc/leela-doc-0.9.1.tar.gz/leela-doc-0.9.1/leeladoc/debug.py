#!/usr/bin/env python3

import os
import sys

from flasket.middleware.flask import FlasketCLIHelper

if __package__ is None and not hasattr(sys, "frozen"):
    path = os.path.realpath(os.path.abspath(__file__))
    path = os.path.dirname(os.path.dirname(path))
    sys.path.insert(0, path)

if __name__ == "__main__":
    FlasketCLIHelper("leeladoc").run(rootpath=__file__)

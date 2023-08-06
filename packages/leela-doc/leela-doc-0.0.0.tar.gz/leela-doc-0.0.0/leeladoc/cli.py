import argparse
import sys

def options(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    # TODO

    return vars(parser.parse_args(argv))


def main():
    args = options()
    # TODO


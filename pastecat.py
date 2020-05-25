#! /usr/bin/env python3

import os
import sys
import argparse
from PIL import ImageGrab, Image

__version__ = '0.0.1'

Image.init()
image_formats = sorted(set(Image.EXTENSION.values()))

parser = argparse.ArgumentParser(
    description="Paste clipboard image to file on Windows/macOS."
)

parser.add_argument(
    "filename",
    nargs="?",
    default="-",
    help="Output filename. If the filename is `-`, image is written to stdout.",
)

parser.add_argument(
    "-f",
    dest="format",
    nargs="?",
    default="",
    choices=image_formats,
    help="Output file format. Default is PNG. If not specified, format is determined from the filename.",
)

parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')

def main():
    args = parser.parse_args()
    format = args.format
    if not format:
        if args.filename != "-":
            ext = os.path.splitext(args.filename)[1].lower()
            format = Image.EXTENSION.get(ext)
            if not format:
                print("Unkown file extension:", ext, file=sys.stderr)
                sys.exit(1)

    if not format:
        format = "PNG"

    img = ImageGrab.grabclipboard()
    if not img:
        print("Clipboard content is not image data.", file=sys.stderr)
        sys.exit(1)

    if args.filename == "-":
        fp = sys.stdout.buffer
    else:
        fp = open(args.filename, "wb")

    img.save(fp, format=format)

    if args.filename != "-":
        fp.close()

if __name__ == "__main__":
    main()

# pastecat

Paste clipboard image to file on Windows/macOS.

## Requirements

- Runs on Windows/macOS.

  **Sorry, I have not test on Windows yet**

- Requires Python 3.7 or later.


## Install

pip3 install pastecat


## Usage


```
usage: pastecat.py [-h]
                   [-f [{BLP,BMP,BUFR,CUR,DCX,DDS,DIB,EPS,FITS,FLI,FTEX,GBR,
                         GIF,GRIB,HDF5,ICNS,ICO,IM,IPTC,JPEG,JPEG2000,MPEG,
                         MPO,MSP,PALM,PCD,PCX,PDF,PIXAR,PNG,PPM,PSD,SGI,SUN,
                         TGA,TIFF,WEBP,WMF,XBM,XPM}]]
                   [--version]
                   [filename]

Paste clipboard image to file onWindows/macOS.

positional arguments:
  filename              Output filename. If the filename is `-`, image is written to stdout.

optional arguments:
  -h, --help            show this help message and exit
  -f [{BLP,BMP,BUFR,CUR,DCX,DDS,DIB,EPS,FITS,FLI,FTEX,GBR,GIF,GRIB,HDF5,
       ICNS,ICO,IM,IPTC,JPEG,JPEG2000,MPEG,MPO,MSP,PALM,PCD,PCX,PDF,PIXAR,
       PNG,PPM,PSD,SGI,SUN,TGA,TIFF,WEBP,WMF,XBM,XPM}]
                        Output file format. Default is PNG. If not specified,
                        format is determined from the filename.
  --version             show program's version number and exit
``` 

## License

Copyright 2020 Atsuo Ishimoto

See LICENSE for detail.

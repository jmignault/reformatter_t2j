# Reformatter_t2j #

Python script to create access derivatives in a folder. The script
creates the files in place. A timestamped logfile is written to the
directory the script is run from.

The script itself can be in any directory, but must be run from the
directory containing the directory to convert:

`c:\Documents> python c:\reformatter_t2j.py testfiles`

for example.

The script requires that `magick` be installed. `magick` is a
headless executable which is part of the default installation of
[ImageMagick.](https://www.imagemagick.org "ImageMagick site")

Once installed magick needs to be on the executable path. This is
done by appending the magick directory to the PATH environment
variable. For example, on Windows, this would be done by typing the
following in a CMD shell:

`set PATH=%PATH%;C:\Program Files\ImageMagick\magick`

The script requires Python 3 and uses only standard Python 3
libraries. It was developed and tested using Python 3.7.3.

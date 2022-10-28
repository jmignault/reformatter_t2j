# Reformatter #

Python script to convert files in a folder. The script creates a
directory in the current directory named 'processed.' The input
directory is mirrored inside the processed directory and converted
files are written to the same location as in the input directory. A
timestamped logfile is written to the top of the processed directory.

The script itself can be in any directory, but must be run from the
directory containing the directory to convert:

`c:\Documents> python c:\reformatter.py testfiles`

for example.

The script requires that `soffice` be installed. `soffice` is a
headless executable which is part of the default installation of
[LibreOffice.](https://www.libreoffice.org "LibreOffice site")

Once installed soffice needs to be on the executable path. This is
done by appending the soffice directory to the PATH environment
variable. For example, on Windows, this would be done by typing the
following in a CMD shell:

`set PATH=%PATH%;C:\Program Files\LibreOffice\program`

The script requires Python 3 and uses only standard Python 3
libraries. It was developed and tested using Python 3.7.3.

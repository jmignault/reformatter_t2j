# Reformatter #

Python script to convert files to PDF in a folder. PDFs are written to
a subfolder named 'processed' and a timestamped log is kept in the
initial folder.

The script requires that `soffice` be installed. `soffice` is a
headless executable which is part of the default installation of
[LibreOffice.](https://www.libreoffice.org "LibreOffice site")

Once installed soffice needs to be on the executable path. This is
done by appending the soffice directory to the PATH enviromnet
variable. For example, on Windows, this would be done by typing the
following in a CMD shell:

`set PATH=%PATH%;C:\Program Files\LibreOffice\program`

On Windows, the directory parameter needs to be a full double-quoted
path.

The script works with standard Python 3 libraries and requires Python
3.

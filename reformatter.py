#!/usr/bin/env python
import os
import argparse
import datetime
from pathlib import Path

# converter functions. Must take 2 arguments: filename and output directory.
def tif_to_jpx(fn, pdir):
   outfn = f'{Path(fn).stem}.jp2'
   outf = os.path.join(pdir, outfn)
   print(outf)
   cmdstr = f'magick {fn} {outf}'
   os.system(cmdstr)

  
# dictionary of format conversions: keys are extensions, value is function to call for conversion 
formats = {'.tif': tif_to_jpx}

# make a list of extensions
fkeys = list(formats.keys())
# define arguments and parse them
parser = argparse.ArgumentParser(description='Walk a folder, converting TIFF files to JP2 format.')
parser.add_argument('infiles', help="Folder containing files to be converted")

args = parser.parse_args()

tstamp = datetime.date.strftime(datetime.datetime.now(), "%m%d%y%M%S")
dname = os.path.basename(os.path.normpath(args.infiles))
logfn = os.path.join(f"{tstamp}_{dname}_log.txt")

logf = open(logfn, 'w', encoding="utf-8")

for path, subdir, files in os.walk(args.infiles):

   for name in files:
      # get a full path to pass to function
      fn = os.path.join(path, name)
      # get the file extension
      ext = os.path.splitext(fn)[-1].lower()
      # calculate a timestamp for the logfile
      lstamp = datetime.date.strftime(datetime.datetime.now(), "%m-%d-%y:%M:%S")
 
      # does file need conversion?
      if ext in fkeys:
         # yes, print a msg & call function associated with the extension
         try:
            print(f"Converting {fn}")
            formats[ext](fn, path)
            logstr = f"{lstamp}: Converted {fn} to jp2\n"
            logf.write(logstr)
         except BaseException as err:
            logf.write(f"{lstamp}:Could not convert {fn}: {err}")
         continue
      # not converting, log that file was skipped
      else:
         logf.write(f"{lstamp}: Skipped {fn}\n")

logf.close()



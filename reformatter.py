#!/usr/bin/env python
import os
import argparse
import datetime

# array of types to be converted
fexts = ('.doc', '.docx')
# define arguments and parse them
parser = argparse.ArgumentParser(description='Convert a folder of files to pdf format.')
parser.add_argument('infiles', help="Folder containing files to be converted")

args = parser.parse_args()

outpath = os.path.join(args.infiles, "processed")
if not (os.path.exists(outpath)):
   os.mkdir(outpath)

tstamp = datetime.date.strftime(datetime.datetime.now(), "%m%d%y%M%S")
logfn = f"{args.infiles}/{tstamp}_processing_log.txt"

logf = open(logfn, 'w')

for fn in os.listdir(args.infiles):
   ext = os.path.splitext(fn)[-1].lower()
   if ext in fexts:
      try:
         lstamp = datetime.date.strftime(datetime.datetime.now(), "%m-%d-%y:%M:%S")
         print(f"Converting {fn}")
         cmdstr = 'soffice --convert-to pdf --outdir "' + outpath + '" "' + args.infiles + '/' + fn + '"'
         os.system(cmdstr)
         logstr = f"{lstamp}: Converted {fn} to pdf\n"
         logf.write(logstr)
      except BaseException as err:
         logf.write(f"{lstamp}:Could not convert {fn}: {err}")
      continue

logf.close()

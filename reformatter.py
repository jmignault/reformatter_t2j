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

outpath = os.path.join(args.infiles, "../processed")
if not (os.path.exists(outpath)):
   os.mkdir(outpath)

tstamp = datetime.date.strftime(datetime.datetime.now(), "%m%d%y%M%S")
dname = os.path.basename(os.path.normpath(args.infiles))
logfn = os.path.join(outpath, f"{tstamp}_{dname}_log.txt")

logf = open(logfn, 'w')

for path, subdir, files in os.walk(args.infiles):

   procdir = os.path.join(outpath, path)
   if not(os.path.exists(procdir)):
      os.mkdir(procdir)

   for name in files:
      fn = os.path.join(path, name)
      ext = os.path.splitext(fn)[-1].lower()
      lstamp = datetime.date.strftime(datetime.datetime.now(), "%m-%d-%y:%M:%S")
 
      if ext in fexts:
         try:
            print(f"Converting {fn}")
            cmdstr = 'soffice --convert-to pdf --outdir "' + procdir + '" "' + fn + '"'
            os.system(cmdstr)
            logstr = f"{lstamp}: Converted {fn} to pdf\n"
            logf.write(logstr)
         except BaseException as err:
            logf.write(f"{lstamp}:Could not convert {fn}: {err}")
         continue
      else:
         logf.write(f"{lstamp}: Skipped {fn}\n")

logf.close()

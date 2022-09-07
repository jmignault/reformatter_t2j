#!/usr/bin/env python
import os
import argparse
import datetime

# define arguments and parse them
parser = argparse.ArgumentParser(description='Convert a folder of files to pdf format.')
parser.add_argument('infiles', help="Folder containing files to be converted")

args = parser.parse_args()

outpath = os.path.join(args.infiles, "processed")
if not (os.path.exists(outpath)):
   os.mkdir(outpath)

logfn = args.infiles +'/' + datetime.date.strftime(datetime.date.today(), "%m%d%y") + "_processing_log.txt"

logf = open(logfn, 'w')

for fn in os.listdir(args.infiles):
  ext = os.path.splitext(fn)[-1].lower()
  if ext == '.doc':
    try:
      print("Converting " + fn)
      cmdstr = 'soffice --convert-to pdf --outdir "' + outpath + '" "' + args.infiles + '/' + fn + '"'
      print(cmdstr)
      os.system(cmdstr)
      logstr = datetime.date.strftime(datetime.date.today(), "%m%d%y:%M:%S")+ ' Converted ' + fn + ' to pdf\n'
      logf.write(logstr)
    except:
      continue

logf.close()

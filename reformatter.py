#!/usr/bin/env python
import os
import argparse
import comtypes.client
format_code = 17

# define arguments and parse them
parser = argparse.ArgumentParser(description='Convert a folder of files to pdf format.')
parser.add_argument('infiles', help="Folder containing files to be converted")

args = parser.parse_args()

outpath = os.path.join(args.infiles, "processed")
if not (os.path.exists(outpath)):
   os.mkdir(outpath)

word_app = comtypes.client.CreateObject('Word.Application')
word_file = word_app.Documents.Open(file_input)

for fn in os.listdir(args.infiles):
  ext = os.path.splitext(fn)[-1].lower()
  if ext == '.doc':
    output = convert(fn, outpath)
    print(output)

word_file.SaveAs(file_output,FileFormat=format_code)
word_file.Close()
word_app.Quit()



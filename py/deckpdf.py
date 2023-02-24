
#!/usr/local/bin/python3
######################################################################
##        Copyright (c) 2020 Carsten Wulff Software, Norway
## ###################################################################
## Created       : wulff at 2020-5-8
## ###################################################################
##  The MIT License (MIT)
##
##  Permission is hereby granted, free of charge, to any person obtaining a copy
##  of this software and associated documentation files (the "Software"), to deal
##  in the Software without restriction, including without limitation the rights
##  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##  copies of the Software, and to permit persons to whom the Software is
##  furnished to do so, subject to the following conditions:
##
##  The above copyright notice and this permission notice shall be included in all
##  copies or substantial portions of the Software.
##
##  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##  SOFTWARE.
##
######################################################################

import os
import sys
import click
import re
import shutil
import pathlib


#allfiles = dict()

class DeckSetPresentation():

    def __init__(self,filename,outputdir):
        self.filename  = filename
        self.orgdir = os.path.dirname(self.filename)
        self.basename = os.path.basename(filename)
        self.noname = self.basename.replace(".md","")
        ofile = os.path.basename(self.filename)
        self.outputdir = outputdir


    def makePdf(self):

        md_file = os.path.abspath(self.filename)
        out_file = os.path.abspath(self.outputdir) + os.pat.sep +    self.noname + ".pdf"

        scpt = self.outputdir + os.path.sep + self.noname + ".scpt"
        with open(scpt,"w") as fo:
            fo.write(f"""
on run argv
  set md_file to "{md_file}"
  set md_file to POSIX file md_file
  set out_file to "{out_file}"
  set out_file to POSIX file out_file
  tell application "Deckset"
    activate
    open file md_file
    delay 2
    tell document 1
     activate
     export to out_file printAllSteps true includePresenterNotes false
     delay 5
    end tell
    quit
   end tell
end run """)
        cmd = f"osascript < {scpt}"
        print(cmd)
        os.system(cmd)



@click.command()
@click.argument("filename")
@click.argument("outputdir")
def cli(filename,outputdir):
    dsp = DeckSetPresentation(filename,outputdir)
    dsp.makePdf()

if(__name__ == "__main__"):
    cli()

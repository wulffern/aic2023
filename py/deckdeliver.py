
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
        odir = outputdir + os.path.sep + ofile.replace(".md","")
        self.outputdir = odir
        self.opath = self.outputdir + os.path.sep + ofile
        self.files = dict()

    def replaceInLine(self,match,line,cnt):
        if not line:
            return line

        
        if(re.search("https?://",line)):
            return line

        
        cppath = match.replace("..","")
        cppath = cppath.replace("/","_")
        cppath = cppath.lstrip("_")

        str_from = self.orgdir + os.path.sep + match
        str_to = self.outputdir + os.path.sep + cppath
        str_already_copied = self.outputdir + os.path.sep  + "../" + match


        if(os.path.exists(str_already_copied)):
            return line
            str_from = str_already_copied
        #cppath =
        #print(match)
        line =line.replace(match,cppath)

        if(cppath not in self.files):
            self.files[cppath] = dict()
            self.files[cppath]["from"] = str_from
            self.files[cppath]["to"] = str_to
            self.files[cppath]["line"] = cnt

        return line

    def makePdf(self):

        md_file = os.path.abspath(self.opath)
        out_file = os.path.abspath(self.outputdir) + os.path.sep + "../" +  self.noname + ".pdf"

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
    tell document 1
     activate
     export to out_file printAllSteps true includePresenterNotes false
    end tell
    quit
   end tell
end run """)
        cmd = f"osascript < {scpt}"
        print(cmd)
        os.system(cmd)

    def copyFiles(self):

        pathlib.Path(self.outputdir).mkdir(parents=True, exist_ok=True)
        

        with open(self.filename,"r") as fi:
            with open(self.opath,"w") as fo:
                cnt = 1
                for line in fi:
                    #print(line)
                    ms= re.findall(r"\[[^\]]*\]\(([^\)]+)\)",line)
                    if(ms):
                        for match in ms:
                            line = self.replaceInLine(match,line,cnt)
                    #print(line)
                    fo.write(line)
                    cnt += 1

        for key in self.files:
            try:
                shutil.copy(self.files[key]["from"],self.files[key]["to"])
            except Exception as e:
                print("ERROR (line " + str(self.files[key]["line"]) + " in " + self.filename + ") " +str(e))


    def deliver(self,pdf):
        self.copyFiles()
        if(pdf):
            self.makePdf()


@click.command()
@click.argument("filename")
@click.argument("outputdir")
@click.option("--pdf/--no-pdf",default=False,help="Write PDF file from deckset")
def cli(filename,outputdir,pdf):
    dsp = DeckSetPresentation(filename,outputdir)
    dsp.deliver(pdf)

if(__name__ == "__main__"):
    cli()

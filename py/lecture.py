#!/usr/bin/env python3

import re
import os
import click
from sys import platform
import shutil

class Image():

    def __init__(self,imgsrc,options):
        self.src = imgsrc
        self.orgsrc = imgsrc
        self.options = options
        self.directory = options["dir"]
        self.skip = False

        if("/ip/" in self.src):
            self.skip = True


        if(not self.skip and ".pdf" in self.src):
            png = self.src.replace(".pdf",".png")

            if(os.path.exists(os.path.join(self.directory,png))):
                self.src = png
            else:
            #if(True):
                if platform == "linux" or platform == "linux2":
                    os.system(f"cd {self.directory};gs -dSAFER -r600 -sDEVICE=pngalpha -o {png} {self.src}")
                elif platform == "darwin":
                    os.system(f"cd {self.directory};sips -s format png {self.src} --resampleHeightWidthMax 800 --out {png}")
                self.src = png

        self.filesrc = os.path.basename(self.src)
        self.dirsrc  = os.path.dirname(self.src)




    def copy(self):
        if(self.skip):
            return

        if("jekyll" in self.options):
            shutil.copyfile(os.path.join(self.options["dir"],self.src), "docs/assets/" + self.filesrc)
        
    def __str__(self):

        if(self.skip):
            return f"> image {self.src} removed"

        if("jekyll" in self.options):
            path = self.options["jekyll"] + "assets/" + self.filesrc

            return f"![]({path})\n"

        return self.src

class Lecture():
    
    def __init__(self,filename,options):
        self.filename = filename
        self.title = ""
        self.options = options
        self.images = list()

        self.filters = {
            "^\s*---\s*$" : "",
            "\[.column\]" : "",
            "\[\.background.*\]" : "",
            "\[\.text.*\]" : "",
            "\[\.table  *\]" : "",
            "\#\s*\[\s*fit\s*\]" : "## ",
            "^## \*\*Q:\*\*.*$" : "",
            "^[.table.*]$": "",
            "#(.*) Thanks!" : ""
        }

        self._read()

    def copyAssets(self):
        with open("images.txt","a") as fo:
            for image in self.images:
                if(not image.skip):
                    fo.write(image.orgsrc + "\n")
                    fo.write(image.src +"\n")
                image.copy()


    def _read(self):

        self.buffer = list()
        first = True
        self.output = False
        self.skipslide = False
        self.removeComment = False

        with open(self.filename) as fi:
            for line in fi:

                if(first and re.search(r"^\s*$",line)):
                    first = False
                    self.output = True


                line = self._readPan(line)

                if(line):
                    line = self._filterLine(line)
                    line = self._convertImage(line)


                if(line is not None and self.output):
                    self.buffer.append(line)



    def _readPan(self,line):

        #- Check pan tags
        m = re.search(r"<!--pan_([^:]+):(.*)$",line)
        if(m):
            key = m.groups()[0]
            val = m.groups()[1]


            if(key == "title"):
                self.title = val.replace("-->","")

            elif(key == "skip"):
                self.skipslide = True
                self.output = False

            elif(key == "doc"):
                 # Start statemachine
                # 1. Skip this line, it should be <!--pan_doc:
                # 2. Enable removing -->
                # 3. When -->, assume that's the end of the pan_doc, and go back to normal
                self.removeComment = True
            else:
                print(f"Uknown key {key}")

            return None

        #- Go back to normal mode
        if(self.removeComment and re.search("-->",line)):
            self.removeComment = False
            return None

        if(self.skipslide and re.search("^\s*---\s*$",line)):
            self.output = True
        return line

    def _convertImage(self,line):
        m = re.search(r"\!\[([^\]]*)\]\(([^\)]+)\)",line)

        if(m):
            imgsrc = m.groups()[1]
            if(re.search("\s*https://",imgsrc)):
                return f"![]({imgsrc})"

            i = Image(imgsrc,self.options)
            self.images.append(i)
            line = str(i)
        return line


    def _filterLine(self,line):
        for r,s in self.filters.items():
            line = re.sub(r,s,line)
        return line

    def __str__(self):

        ss = ""

        if("jekyll" in self.options):

            slides = ""
            if("lectures" in self.filename ):
                slides = "[Slides][" +  self.options["jekyll"] + self.filename.replace("lectures","slides").replace(".md",".html") +"]"

            ss += f"""---
layout: post
title: {self.title}
math: true
---

{slides}

""" + """



* TOC
{:toc }

"""

        for l in self.buffer:
            ss += l
        return ss

class Presentation(Lecture):

    def __init__(self,filename,options):
        self.filename = filename
        self.title = filename.replace(".md","")
        self.options = options

        self.images = list()

        self.filters = {
            "\[\.background.*\]" : "",
            "\[\.text.*\]" : "",
            "\[\.table  *\]" : "",
            "\#\s*\[\s*fit\s*\]" : "## ",
            "^[.table.*]$": "",
            "\!\[[^\]]+\]" : "![]",
            "^# ":"## ",
            "\[.column\]" : "",
            #"^---":"#",

        }

        self._read()

    def _read(self):

        self.buffer = list()
        first = True
        self.output = False
        self.skipslide = False
        self.removeComment = False

        with open(self.filename) as fi:
            for line in fi:

                if(first and re.search(r"^\s*$",line)):
                    first = False
                    self.output = True

                key = ""
                val = ""
                m = re.search(r"<!--pan_([^:]+):(.*)$",line)
                if(m):
                    key = m.groups()[0]
                    val = m.groups()[1]


                if(key == "title"):
                    self.title = val.replace("-->","")

                if(re.search("^<!--",line)):
                    self.output = False

                line = self._filterLine(line)
                line = self._convertImage(line)

                if(line is not None and self.output):
                    self.buffer.append(line)

                if(re.search("-->",line)):
                    self.output = True

    def __str__(self):

        ss = ""

        ss += f"""---
title: {self.title}
output:
  slidy_presentation:
    footer: "Copyright (c) 2023, Carsten Wulff"
    fig_width: 800
---

""" + """




"""
        for l in self.buffer:
            ss += l
        return ss



    

@click.group()
def cli():
    """
    Convert a lecture to something
    """
    pass

@cli.command()
@click.argument("filename")
@click.option("--root",default="/aic2023/",help="Root of jekyll site")
@click.option("--date",default="2023-01-01",help="Date to use")
def post(filename,root,date):
    options = dict()
    options["jekyll"] = root
    options["dir"] = os.path.dirname(filename)

    #- Post
    l = Lecture(filename,options=options)
    l.copyAssets()
    fname = "docs/_posts/" + date +"-"+ l.title.strip().replace(" ","-") + ".markdown"

    with open(fname,"w") as fo:
        fo.write(str(l))
    


@cli.command()
@click.argument("filename")
@click.option("--root",default="/aic2023/",help="Root of jekyll site")
def slide(filename,root):
    options = dict()
    options["jekyll"] = root
    options["dir"] = os.path.dirname(filename)
    p = Presentation(filename,options)
    p.copyAssets()
    fname = "slides/" + os.path.basename(filename)

    with open(fname,"w") as fo:
        fo.write(str(p))

    fhtml = fname.replace(".md",".html")
    cmd = f"pandoc -t slidy --slide-level 0 -s {fname} -o docs/{fhtml} "
    print(cmd)
    os.system(cmd)




if __name__ == "__main__":
    cli()

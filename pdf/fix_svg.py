#!/usr/bin/env python3

import re
import sys
import os
fname = sys.argv[1]
foname = fname.replace(".latex","_fiximg.tex")

tmplta = r"""
\begin{figure}[h]
\centering
\includegraphics[width=\myfigwidth]{#path#}
\end{figure}
"""

tmplt = r"""
{
\centering
\includegraphics[width=\myfigwidth]{#path#}

}
"""


with open(foname,"w") as fo:
    with open(fname) as fi:
        for line in fi:
            if(re.search("includegraphics.*\.svg}",line)):
                #print(line)
                m = re.findall("{([^}]+)}",line)
                path = m[0]
                #if(re.search("http",path)):
                #    os.system(f"cd media && wget {path}")
                fopath = "media/"+ os.path.basename(path).replace(".svg",".pdf")
                if(not os.path.exists(fopath)):
                    os.system(f"svg2pdf -o {fopath} {path}")
                line = line.replace(path,fopath)
                #line = re.sub("includegraphics","includesvg",line)
            elif(re.search("includegraphics.*\.gif",line)):
                m = re.findall("{([^}]+)}",line)
                path = m[0]
                fopath = "media/"+ os.path.basename(path).replace(".gif",".png")
                if(not os.path.exists(fopath)):
                    os.system(f"convert {path} {fopath}")
                line = line.replace(path,fopath)

            if(re.search("includegraphics{",line)):
                m = re.findall("{([^}]+)}",line)
                path = m[0]
                line = tmplt.replace("#path#",path)
                #line = line.replace("includegraphics{","includegraphics[width=\myfigwidth]{")

            fo.write(line)

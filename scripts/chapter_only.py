#!/usr/bin/env python3
"""Compile a single chapter quickly: python3 scripts/chapter_only.py 9"""
import sys,glob,subprocess,os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
n=int(sys.argv[1]); f=glob.glob(f"{root}/chapters/ch{n:02d}_*.tex")[0]
base=os.path.basename(f)[:-4]
open(f"{root}/_one.tex","w").write(r"""\documentclass[10pt,twoside,openany]{book}
\input{preamble}\input{macros}
\begin{document}
\setcounter{chapter}{%d}\addtocounter{chapter}{-1}
\input{chapters/%s}
\end{document}
"""%(n,base))
subprocess.run(["latexmk","-pdf","-interaction=nonstopmode","_one.tex"],cwd=root)

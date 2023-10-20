
VERSION_DATE=Built on $(shell date)
VERSION_HASH=${shell git log -1 --pretty=format:"%H"}
FILE= aic

TEXS = ${shell ls -1 tex/*.latex}

fix:
	${foreach f, ${TEXS}, python3 fix_svg.py ${f};}

hash:
	echo '{\\noindent ${VERSION_DATE}} \\\\ \n {\\noindent from ${VERSION_HASH}}'  > tex/version.tex

one: fix hash
	ls -l tex/
	ls -l tex/media
	-pdflatex -interaction nonstopmode --shell-escape aic.latex
	-bibtex aic.latex
	-pdflatex -interaction nonstopmode --shell-escape aic.latex

compress:
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
	-dNOPAUSE -dQUIET -dBATCH -sOutputFile=aic_compress.pdf aic.pdf

ebook:
	pandoc --gladtex -o aic.epub aic.latex

clean:
	-rm *.bbl
	-rm *.aux
	-rm *.toc
	-rm *.log
	-rm *.blg
	-rm *.dvi
	-rm *.fff
	-rm *.lof
	-rm *.lot
	-rm *.ttt
	-rm *.xml
	-rm *.pdf
	-rm *.bcf

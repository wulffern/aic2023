
VERSION_DATE=Built on $(shell date)
VERSION_HASH=${shell git log -1 --pretty=format:"%H"}
FILE= aic

TEXS = ${shell ls -1 *.latex}

fix:
	${foreach f, ${TEXS}, python3 fix_svg.py ${f};}

hash:
	echo '{\\noindent ${VERSION_DATE}} \\\\ \n {\\noindent from ${VERSION_HASH}}'  > version.tex

one: fix hash
	chmod -R 755  media
	pdflatex aic.latex
	#-pdflatex -interaction nonstopmode --shell-escape aic.latex
	bibtex aic.latex
	pdflatex aic.latex
	#-pdflatex -interaction nonstopmode --shell-escape aic.latex

compress:
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
	-dNOPAUSE -dQUIET -dBATCH -sOutputFile=aic_compress.pdf aic.pdf

ebook:
	cat aic.latex |perl -pe "s/fiximg/fiximg_png/ig" > aic_epub.latex
	pandoc --gladtex -o aic.epub aic_epub.latex

clean:
	-rm *.latex
	-rm *_fiximg.tex
	-rm *.md
	-rm -rf media
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

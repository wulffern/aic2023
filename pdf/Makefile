

FILE= aic

TEXS = ${shell ls -1 tex/*.latex}

fix:
	${foreach f, ${TEXS}, python3 fix_svg.py ${f};}

one: fix
	-pdflatex -interaction nonstopmode --shell-escape aic.latex
	-bibtex aic.latex
	-pdflatex -interaction nonstopmode --shell-escape aic.latex
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
	-dNOPAUSE -dQUIET -dBATCH -sOutputFile=aic_book.pdf aic.pdf

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

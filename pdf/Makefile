

FILE= aic

TEXS = ${shell ls -1 tex/*.latex}

fix:
	${foreach f, ${TEXS}, python3 fix_svg.py ${f};}

one: fix
	-pdflatex -interaction nonstopmode --shell-escape aic.latex
	-bibtex aic.latex
	-pdflatex -interaction nonstopmode --shell-escape aic.latex

ebook:
	pandoc -o aic.epub tex/lecture_1_-__introduction.md \
		tex/a_refresher.md \
		tex/diodes.md

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

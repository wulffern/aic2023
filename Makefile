
JEKYLL_VERSION=3.8
SITE=${shell pwd}/docs

.PHONY:  slides

FILES = l01_intro \
	l01_need_to_know \
	l02_esd \
	l03_refbias \
	l04_afe \
	l05_sc \
	l06_adc

pan:
	./d2pan

note:
	rm -rf deliv_notes
	mkdir deliv_notes
	mv pandoc/*.pdf deliv_notes

mpdf:
	gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=aic2022.pdf deliv_notes/*.pdf

cpm:
	cp ../dic_2021/dic2021/media/${FILE} media/

jstart:
	docker run --rm --name aic_docs --volume="${SITE}:/srv/jekyll" -p 3002:4000 -it jekyll/jekyll:${JEKYLL_VERSION} jekyll serve --watch --drafts

posts:
	./genposts.sh
	cd lectures; cat ../images.txt |xargs git add -f

slides:
	${foreach f, ${FILES}, ${MAKE} slide FILE=$f; }

slide:
	python3 py/deckpdf.py lectures/${FILE}.md docs/slides/


JEKYLL_VERSION=3.8
SITE=${shell pwd}/docs

.PHONY:  slides

FILES = lectures/tex_intro memos/2021-07-08_diodes/memo \
	docs/_posts/2023-01-09-Refresher  \
	lectures/l01_intro \
	lectures/l02_esd \
	lectures/l03_refbias \
	lectures/l04_afe \
	lectures/l05_sc \
	lectures/l06_adc \
	lectures/l07_vreg \
	lectures/l08_pll \
	lectures/l09_osc \
	lectures/l10_lpradio \
	lectures/l11_aver \
	lectures/lx_energysrc

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

latex:
	${foreach f, ${FILES}, python3 py/lecture.py latex ${f}.md ; }
	cd pdf; make one

book:
	cd pdf; make book

slides:
	${foreach f, ${FILES}, ${MAKE} slide FILE=$f; }


slide:
	python3 py/deckpdf.py ${FILE}.md docs/slides/

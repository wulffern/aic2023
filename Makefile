
JEKYLL_VERSION=3.8
SITE=${shell pwd}/docs

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

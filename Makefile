
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

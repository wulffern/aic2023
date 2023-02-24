
lectures = l01_intro.md \
	l03_refbias.md \
	l04_afe.md



addimg:
	$(foreach l,${lectures}, cat $l |perl -ne 'if(m/!\[.*\]\((.*)\)/ig){ $$i=$$1; unless($$i =~ m/\/ip\/|https/ig){ print $$1."\n";}}'|xargs git add;)

clean:
	rm *.nav
	rm *.aux
	rm *.log
	rm *.out
	rm *.snm
	rm *.toc
	rm *.tex

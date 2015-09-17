NAME = example

LATEX = xelatex
BIBTEX = bibtex

.PHONY: all clean latex bibtex render

default: all

all: ${NAME}.pdf

render: ${NAME}.tex

latex: render
	${LATEX} ${NAME}

bibtex: latex
	${BIBTEX} ${NAME}

%.pdf: %.tex
	${LATEX} $<
	-${BIBTEX} $(basename $< .tex) && ${LATEX} $< && ${LATEX} $<

%.tex: %.tex.tpl config.py
	python render.py $< > $(basename $< .tpl)

clean:
	rm -rf $(shell cat .gitignore)

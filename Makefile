all: main.pdf
main.pdf: main.tex $(wildcard chapters/*.tex) $(wildcard parts/*.tex) $(wildcard appendices/*.tex) preamble.tex macros.tex refs.bib
	python3 scripts/gen.py
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
# build ONE chapter fast:  make ch N=10
ch:
	python3 scripts/chapter_only.py $(N)
clean:
	latexmk -C

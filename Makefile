all: build/main.pdf

# hier Python-Skripte:

build/raumtemp.pdf: raumtemp.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python raumtemp.py
build/messreihe2.pdf: messreihe2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python messreihe2.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/raumtemp.pdf build/messreihe2.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean

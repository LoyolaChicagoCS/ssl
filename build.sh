[ -f ~/.env/sphinx/bin/activate ] && . ~/.env/sphinx/bin/activate

make clean
make html
make LATEXOPTS=' -interaction=batchmode ' latexpdf
make epub

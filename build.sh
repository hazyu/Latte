#/bin/bash

nuitka --standalone --onefile --remove-output --include-data-dir=templates=templates --include-data-dir=static=static --include-data-file=mocha=mocha main.py -o main
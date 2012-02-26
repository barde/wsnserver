#!/bin/bash

pdflatex wsnserver && pdflatex wsnserver && bibtex wsnserver  && pdflatex wsnserver

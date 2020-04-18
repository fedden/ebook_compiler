#!/bin/bash
# Concatenate all markdown files.
python3 ./scripts/concatenate.py --markdown_dir $1 
# Create output directory if it doesn't exist already.
mkdir -p output
# Convert markdown files to pdfs.
FIGURES=$(find $1 -name "*.svg")
pandoc build/$1.md $FIGURES -o output/$1.pdf \
    --table-of-contents                      \
    --pdf-engine=xelatex                     \
    --from=markdown                          \
    --number-sections                        \
    --highlight-style=pygments               \
    -V mainfont="Palatino"                   \
    -V documentclass=report                  \
    -V papersize=A5                          \
    -V geometry:margin=1in
# Open resultant pdf file.
open output/$1.pdf
# Print out that we updated the file.
MARKDOWN_FILES=$(find $1 -name "*.md")
TEXT="detected changes to one of [$MARKDOWN_FILES], updated output/$1.pdf"
echo ${TEXT//\\n/}

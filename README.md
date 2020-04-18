# Book base template

This repo is a barebones system to build a book from a collecton of markdown files.

### Installation

This is designed for OS X, but could be adapted for other operating systems such as Linux by modifying the `open` call in the `scripts/convert_and_open.sh`. The code requires python3 to be installed system wide.

In addition, both `xelatex` and `pandoc` are required to build the book.

Finall, the tool `fswatch` [will also need to be installed.](https://github.com/emcrisostomo/fswatch)

### Usage 

The idea is to write chapters as seperate markdown files. Each chapter should have the number in the file name, e.g for chapter one, for a book name called `book_name`, we'd store the file as `./book_name/chapter_name_1.md`.

To build the book any time a markdown file is modified, please run `./scripts/watch book_name`. This will watch for the changes and rebuild the book as `book_name.pdf` in the `output` directory. 

### Accreditation

[This is all based on this excellent blog post.](https://keleshev.com/my-book-writing-setup/)

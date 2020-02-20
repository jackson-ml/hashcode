import sys


def write_out(output_file, library_order, book_order):
    lib_order_string = ' '.join(str(lib) for lib in  library_order)
    book_order_strings = [' '.join(str(book) for book in i) for i in book_order]
    lines = [str(len(library_order))]
    with open(output_file, 'w') as out:
        
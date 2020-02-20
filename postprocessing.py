import sys
from score_libraries import get_library_order
from book_order import get_book_order


def write_out(output_file, library_order, book_order):
    book_order_strings = {lib_id: ' '.join(str(book) for book in book_order) for lib_id,
                                                                book_order in
                          book_order.items()}
    lines = [str(len(library_order))]
    for lib in library_order:
        first_line = f'{lib.lib_id} {len(lib)}'
        second_line = book_order_strings[lib.lib_id]
        lines.append(first_line)
        lines.append(second_line)
    with open(output_file, 'w') as out:
        out.write("\n".join(lines))


if __name__ == "__main__":
    input_filename = sys.argv[1]
    out_filename = sys.argv[2]
    library_order, book_scores = get_library_order(input_filename)
    book_order = get_book_order(library_order, book_scores)
    write_out(sys.argv[2], library_order, book_order)
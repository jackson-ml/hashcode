from score_libraries import *


def get_book_order(input_file):
    library_order, book_scores = get_library_order(input_file)
    book_order = []
    scanned_books = set()

    for library in library_order:
        all_books = set(library.books)

        duplicated_books = all_books.intersection(scanned_books)
        books_to_scan = list(all_books.difference(duplicated_books))

        sorted_book_order = sorted(
            books_to_scan, 
            key=lambda book_id: book_scores[book_id], 
            reverse=True)

        sorted_book_order.extend(list(duplicated_books))
        scanned_books = scanned_books.union(set(sorted_book_order))
        
        book_order.append(sorted_book_order)

    return book_order


if __name__ == "__main__":
    print(get_book_order(sys.argv[1]))
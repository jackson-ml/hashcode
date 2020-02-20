from parse_data import parse_input_file, Library


def unique_books_per_day(library: Library, book_scores, days_left,
                         existing_books):
    days_after_signup = days_left - library.signup
    books_scanned = library.rate * days_after_signup
    unique_books = [i for i in library.books if i not in existing_books]
    unique_books.sort(key=lambda x: book_scores[x], reverse=True)
    scannable_books = unique_books[:books_scanned]
    return sum(book_scores[i] for i in scannable_books)/days_after_signup


def get_library_order(input):
    b, l, d, book_scores, libraries = parse_input_file(input)
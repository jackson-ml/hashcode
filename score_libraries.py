from parse_data import parse_input_file, Library
import sys

def unique_books_per_day(library: Library, book_scores, days_left,
                         existing_books):
    days_after_signup = days_left - library.signup
    if days_after_signup <= 0:
        return 0
    books_scanned = library.rate * days_after_signup
    unique_books = [i for i in library.books if i not in existing_books]
    unique_books.sort(key=lambda x: book_scores[x], reverse=True)
    scannable_books = unique_books[:books_scanned]
    total_score = sum(book_scores[i] for i in scannable_books)
    return total_score


def library_score_over_signup(library: Library, book_scores, days_left,
                              existing_books):
    return unique_books_per_day(library, book_scores, days_left,
                                existing_books) / library.signup


def get_library_order(input_file):
    b, l, d, book_scores, libraries = parse_input_file(input_file)
    days_left = d
    library_order = []
    existing_books = set()
    # for library in libraries:
    #     print(library)
    #     print(library.signup)
    while days_left > 0:
        viable_libraries = [i for i in libraries if i.signup <= days_left]
        if not viable_libraries:
            break
        next_library = max(viable_libraries, key=lambda x:
            library_score_over_signup(x, book_scores, days_left, existing_books))
        library_order.append(next_library)
        libraries.remove(next_library)
        days_left -= next_library.signup
        existing_books.union(set(next_library.books))
    return library_order, book_scores


if __name__ == "__main__":
    print([library.lib_id for library in get_library_order(sys.argv[1])])

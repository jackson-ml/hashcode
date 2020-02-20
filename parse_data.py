

class Library:
    def __len__(self):
        len(self.books)

    def __str__(self):
        return id

    def __init__(self, id, books, signup, rate):
        self.id = id
        self.books = books
        self.signup = signup
        self.rate = rate


def parse_input_file(input):
    with open(input) as input_file:
        bld_string = input_file.readline()
        bld_list = bld_string.split()
        b = int(bld_list[0])
        l = int(bld_list[1])
        d = int(bld_list[2])
        book_score_string = input_file.readline()
        book_scores = [int(i) for i in book_score_string.split()]
        libraries = []
        for i in range(l):
            size_signup_and_rate = [int(i) for i in input_file.readline().split()]
            books = [int(i) for i in input_file.readline().split()]
            library = Library(i+1, books, size_signup_and_rate[1],
                              size_signup_and_rate[2])
            libraries.append(library)
        return b, l, d, book_scores, libraries

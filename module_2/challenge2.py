# Requirements:
# ● Create the dictionary: Begin with creating a dictionary where the keys are tuples of book titles and authors, and the values are genres.
# ● Add a New Book: Add a new entry to the dictionary with a tuple containing the title and author of the new book, and set its genre.
# ● Retrieve and Print Book Information: Retrieve and print the genre of a book given its title and author.


books = {
    ("1984", "George Orwell"): "Dystopian",
    ("To Kill a Mockingbird", "Harper Lee"): "Classic Fiction",
    ("The Hobbit", "J.R.R. Tolkien"): "Fantasy"
}

books [("Blerdon Ibriqi's book", "Belgin Jashari")] : "Histori"


keys = list(books.keys())
title, author = keys[0]
print(title, " was written by ", author)

# List of books in and out
books_in = []
books_out = []

def event():
    print("Would you like to take out, return or donate a book?")
    to_do = int(input("Press 1 to take out, 2 to return, 3 to donate and, 4 to leave the library."))

    # code for if the want to take out a book
    if to_do == 1:
        for book in books_in:
            print("We have " + book)

        book_wanted = input("What book would you like to check out?")
        if book_wanted == "none" or book_wanted == "None":
            print("Ok then.")

            if book_wanted in books_in:

                if book_wanted == "Night":
                    books_out.append("Night")
                    books_in.remove("Night")
                    print("bring it back in one week.")

                if book_wanted == "The Outsiders":
                    books_out.append("The Outsiders")
                    books_in.remove("The Outsiders")
                    print("bring it back in one week.")

                if book_wanted == "The Fortnite Encyclopedia":
                    books_out.append("The Fortnite Encyclopedia")
                    books_in.remove("The Fortnite Encyclopedia")
                    print("bring it back in one week.")

                if book_wanted == "Julius Caesar":
                    books_out.append("Julius Caesar")
                    books_in.remove("Julius Caesar")
                    print("bring it back in one week.")

                else:
                 books_out.append(book_wanted)
                 books_in.remove(book_wanted)


        if book_wanted not in books_in:
            print("We do not carry that book.")

    # code for if they want to return a book
    elif to_do == 2:
        book_return = input("What book are you returning?")

        if book_return == "Night":
            books_in.append("Night")
            books_out.remove("Night")

        elif book_return == "The Outsiders":
            books_in.append("The Outsiders")
            books_out.remove("The Outsiders")

        elif book_return == "The Fortnite Encyclopedia":
            books_in.append("The Fortnite Encyclopedia")
            books_out.remove("The Fortnite Encyclopedia")

        elif book_return == "Julius Caesar":
            books_in.append("Julius Caesar")
            books_out.remove("Julius Caesar")

        elif book_return not in books_in or book_return not in books_out:
            print("We do not carry that book.")

        else:
            books_in.append(book_return)
            books_out.remove(book_return)

    # code for if they want to donate a book
    elif to_do == 3:
        book_donated = input("What is the book you are donating.")
        books_in.append(book_donated)
        print("Thank you for your donation to the Jimmy Foundation Public Library")

    # code for when they want to leave the library
    elif to_do == 4:
        x = 43
        print("Thanks for stopping in at the Jimmy Foundation Public Library.")

    else:
        print("You didn't answer with our system you need to say 1, 2, 3, or 4. Please try again.")

print("Welcome to the Jimmy Foundation Public Library.")

books_in.append("Night")
books_in.append("The Outsiders")
books_in.append("The Fortnite Encyclopedia")
books_in.append("Julius Caesar")

if "Night" in books_in and books_out:
    books_out.remove("Night")

# looping the code
x = 42
while x == 42:
    event()


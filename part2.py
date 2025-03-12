 # Creating a book inventory dictionary
books = {
    "978-3-16-148410-0": ("Python Basics", "Samra", 22.50, {"programming", "technology"}),
    "978-1-234567-89-7": ("Data Science Essentials", "John", 25.50, {"data science", "machine learning"}),
    "978-3-16-123456-2": ("Web Development with Flask", "Jane", 22.90, {"web development", "framework"}),
    "978-5-67-891234-1": ("Advanced Python", "Samra", 30.00, {"programming", "software development"}),
    "978-4-56-789012-3": ("Machine Learning Basics", "John", 28.75, {"data science", "AI"})
}

# Function to search books by author
def search_by_author(author):
    result = []  # List t…
 # Creating a book inventory dictionary
books = {
    "978-3-16-148410-0": ("Python Basics", "Samra", 22.50, {"programming", "technology"}),
    "978-1-234567-89-7": ("Data Science Essentials", "John", 25.50, {"data science", "machine learning"}),
    "978-3-16-123456-2": ("Web Development with Flask", "Jane", 22.90, {"web development", "framework"}),
    "978-5-67-891234-1": ("Advanced Python", "Samra", 30.00, {"programming", "software development"}),
    "978-4-56-789012-3": ("Machine Learning Basics", "John", 28.75, {"data science", "AI"})
}

# Function to search books by author
def search_by_author(author):
    result = []  # List to store matching books

    # Loop through the dictionary
    for isbn, details in books.items():
        title, book_author, _, _ = details  # Extract title and author
        
        # If author matches, add (ISBN, Title) to result
        if book_author.lower() == author.lower():
            result.append((isbn, title))
    
    return result  # Return list of matching books

# Taking author name as input from the user
author_name = input("Enter author name to search: ")

# Searching for books by the given author
matching_books = search_by_author(author_name)

# Printing results
if matching_books:
    print(f"\nBooks written by {author_name}:")
    for isbn, title in matching_books:
        print(f"- ISBN: {isbn} | Title: {title}")
else:
    print(f"No books found by {author_name}.")
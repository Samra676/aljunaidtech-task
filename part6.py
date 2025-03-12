# Creating a book inventory dictionary
books = {
    "978-3-16-148410-0": ("Python Basics", "Samra", 22.50, {"programming", "technology"}),
    "978-1-234567-89-7": ("Data Science Essentials", "John", 25.50, {"data science", "machine learning"}),
    "978-3-16-123456-2": ("Web Development with Flask", "Jane", 22.90, {"web development", "framework"}),
    "978-5-67-891234-1": ("Advanced Python", "Samra", 30.00, {"programming", "software development"}),
    "978-4-56-789012-3": ("Machine Learning Basics", "John", 28.75, {"data science", "AI"})
}

# Function to list and sort all book titles
def list_all_books():
    # Extract all book titles from the dictionary
    titles = [details[0] for details in books.values()]
    
    # Sort the titles alphabetically
    titles.sort()
    
    return titles

# Calling the function and displaying the result
sorted_titles = list_all_books()
print("\nList of All Books (Alphabetically Sorted):")
for title in sorted_titles:
    print(f"- {title}")
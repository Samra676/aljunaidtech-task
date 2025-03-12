# Creating a book inventory dictionary
books = {
    "978-3-16-148410-0": ("Python Basics", "Samra", 22.50, {" Programming ", "Technology "}),
    "978-1-234567-89-7": ("Data Science Essentials", "John", 25.50, {" Data Science ", " Machine Learning"}),
    "978-3-16-123456-2": ("Web Development with Flask", "Jane", 22.90, {" Web Development", " Framework "}),
    "978-5-67-891234-1": ("Advanced Python", "Samra", 30.00, {" Programming", " Software Development "}),
    "978-4-56-789012-3": ("Machine Learning Basics", "John", 28.75, {" Data Science", " AI "})
}

# Function to standardize genres
def standardize_genres():
    for isbn, details in books.items():
        title, author, price, genres = details  # Extract book details

        # Clean and standardize genres (lowercase + strip spaces)
        cleaned_genres = {genre.strip().lower() for genre in genres}

        # Update book entry with cleaned genres
        books[isbn] = (title, author, price, cleaned_genres)

# Calling the function to standardize genres
standardize_genres()

# Display updated book inventory
print("\nUpdated Book Inventory with Standardized Genres:")
for isbn, details in books.items():
    print(f"- ISBN: {isbn} | Title: {details[0]} | Genres: {details[3]}")
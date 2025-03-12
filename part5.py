# Creating a book inventory dictionary
books = {
    "978-3-16-148410-0": ("Python Basics", "Samra", 22.50, {"programming", "technology"}),
    "978-1-234567-89-7": ("Data Science Essentials", "Ali", 25.50, {"data science", "machine learning"}),
    "978-3-16-123456-2": ("Web Development with Flask", "Jane", 22.90, {"web development", "framework"}),
    "978-5-67-891234-1": ("Advanced Python", "Samra", 30.00, {"programming", "software development"}),
    "978-4-56-789012-3": ("Machine Learning Basics", "John", 28.75, {"data science", "AI"})
}

# Function to display the book inventory
def display_inventory():
    print("\n" + "="*90)
    print(f"{'ISBN':<20} {'Title':<30} {'Author':<15} {'Price ($)':<10} {'Genres'}")
    print("="*90)
    
    # Loop through each book in the inventory
    for isbn, (title, author, price, genres) in books.items():
        genre_str = ", ".join(genres)  # Convert set to a comma-separated string
        
        # Print each book's details in formatted columns
        print(f"{isbn:<20} {title:<30} {author:<15} ${price:<9.2f} {genre_str}")
    
    print("="*90)

# Calling the function to display inventory
display_inventory()
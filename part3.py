# Creating a book inventory dictionary
books = {
    "978-3-16-148410-0": ("Python Basics", "Samra", 22.50, {"programming", "technology"}),
    "978-1-234567-89-7": ("Data Science Essentials", "John", 25.50, {"data science", "machine learning"}),
    "978-3-16-123456-2": ("Web Development with Flask", "Jane", 22.90, {"web development", "framework"}),
    "978-5-67-891234-1": ("Advanced Python", "Samra", 30.00, {"programming", "software development"}),
    "978-4-56-789012-3": ("Machine Learning Basics", "John", 28.75, {"data science", "AI"})
}

# Function to update the price of a book
def update_price(isbn, new_price):
    # Check if the ISBN exists in the dictionary
    if isbn in books:
        title, author, _, genres = books[isbn]  # Extract current details
        books[isbn] = (title, author, new_price, genres)  # Update with new price
        print(f"✅ Price updated for '{title}' (ISBN: {isbn}). New Price: ${new_price}")
    else:
        print(f"❌ Error: No book found with ISBN {isbn}.")

# Taking user input for ISBN and new price
isbn_input = input("Enter ISBN to update price: ")
new_price_input = float(input("Enter new price: "))

# Calling the function to update price
update_price(isbn_input, new_price_input)

# Display updated inventory
print("\nUpdated Book Inventory:")
for isbn, details in books.items():
    print(f"- ISBN: {isbn} | Title: {details[0]} | Price: ${details[2]}")
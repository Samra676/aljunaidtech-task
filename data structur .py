# creating an empty dictionary
books={}
# Example of adding a book entry
books['947-3-16-148410_1']=(
"python for beginners",#title
  "samra",# author
  22.50,#price
  {"programming","technology"}# genres (set)
  )
books["876-1-1234567-89-0"]=(
     "data science essentials",
     "john",
     25.50,
     {"data  science ","machine learning"}
 )  
books["564-3-16-123456_2"]=(
    "web development with flask ",
    "jane",
    22.9,
    {"web development", "framework"}
)
for isbn ,details in books.items():
    title, author, price, genres= details
    print(f"ISBN:{isbn}")
    print(f"title:{title}")
    print (f"Author:{author}")
    print(f"price:{price}")
    print(f"genres:{','.join(genres)}")
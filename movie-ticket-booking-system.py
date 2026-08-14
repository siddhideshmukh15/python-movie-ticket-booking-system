movies = {
    "1": {"name": "krishnavantaram", "price": 200},
    "2": {"name": "Alpha", "price": 180},
    "3": {"name": "peddi", "price": 150}
}

print("===== Movie Ticket Booking =====")

print("\nAvailable Movies:")
for key, movie in movies.items():
    print(key, movie["name"], "- ₹", movie["price"])

choice = input("\nSelect movie: ")

if choice in movies:
    movie = movies[choice]

    print("\nYou selected:", movie["name"])
    
    tickets = int(input("Enter number of tickets: "))

    total = tickets * movie["price"]

    print("\n===== Booking Details =====")
    print("Movie:", movie["name"])
    print("Tickets:", tickets)
    print("Total Price: ₹", total)
    print("Booking successful!")

else:
    print("Invalid movie choice!")
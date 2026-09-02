movies ={
    "1": {"name": "Krishnavantaram", "price": 200},
    "2": {"name": "Alpha","price":180},
    "3": {"name": "Peddi","price":150}
}

bookings ={}
booking_count =1

while True:
    print("\n === Movie Ticket Booking System ===")
    print("1. 'View Movies'\n 2.'Book Tickets'\n 3.'View Bookings'\n 4.'Search Bookings'\n 5.'Cancel Bookings'\n 6. 'Exit'")
    
    choice = input("Enter your choice:")
    
    if choice =="1":
        print("\n === Available Movies ===")
        
        for key,movie in movies.items():
            print(key,movie["name"],"- rs", movie["price"])
            
    elif choice =="2":
         print("\n === Available Movies ===")
         for key,movie in movies.items():
             print(key,movie["name"],"- rs", movie["price"])
             
             movie_choice = input("\n Select movie:")
             
             if movie_choice in movies:
                 movie = movies[movie_choice]
                 
                 name = input("Enter your name:")
                 phone= input("Enter phone number:")
                 tickets = int(input("Enter number of tickets:"))
                 
                 total =tickets*movie["price"]
                 booking_id="B"+str("booking_count")
                 booking_count +=1
                 
                 bookings[booking_id]= {
                     "Name":name,
                     "phone":phone,
                     "movie":movie["name"],
                     "tickets": tickets,
                     "total": total
                 }
                 print("\n=== Booking Sucessful ===")
                 print("Booking ID:",booking_id)
                 print("Name:name")
                 print("Movie:",movie["name"])
                 print("Tickets:",tickets)
                 print("Total price: rs",total)
                 
             else:
                 print("Invalid movie choice!")
                 
    elif choice =="3":
        if not bookings:
            print("\n No bookings found!")
            
        else:
            print("\n=== All Bookings ===")
            
            for booking_id, booking in bookings.items():
                print("\n=== Booking Sucessful ===")
                print("Booking ID:",booking_id)
                print("Name:name")
                print("Movie:",movie["name"])
                print("Tickets:",bookings["tickets"])
                print("Total price: rs",bookings["total"])
                
    elif choice =="4":
        booking_id= input("Enter booking ID:")
        
        if booking_id in bookings:
            booking =bookings[booking_id]
            print("\n=== Booking Found ===")
            print("Booking ID:",booking_id)
            print("Name:name")
            print("Movie:",movie["name"])
            print("Tickets:",bookings["tickets"])
            print("Total price: rs",bookings["total"])
            
        else:
            print("Booking not found!")
            
    elif choice =="5":
        booking_id =input("Enter booking ID to cancel:")
        
        if booking_id in bookings:
            del bookings[booking_id]
            print("Booking cancelled sucessfully!")
            
        else:
            print("Booking not found!")
            
    elif choice =="6":
        print("Thank you for using Movie Ticket Booking System")
        break
    
    else:
        print("Invalid choice!")
                            
            
                
                 
        
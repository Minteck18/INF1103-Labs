#q1
inventory = 0; 
total = 0

#q2
while True:
    stock_quantity = input("Please enter the stock quantity or type quit to exit")
    try:
       #q2
       if stock_quantity.lower() == "quit":
           print("You have exited from the program, bye")
           break
       # q3
       stock_quantity = int(stock_quantity)
       #q6
       if stock_quantity > 0:
               total += int(stock_quantity) 
               print("current running total", total)
       #q5
       if stock_quantity < 0: 
            print("Negative numbers are not allowed!")

       #q7
       if total > 500:
            print("The inventory has exceed 500 units!")
            break
       
    except:
        #q4
        if stock_quantity != stock_quantity.isdigit():
            print("Invalid input! Please enter a integer")
     

    
    


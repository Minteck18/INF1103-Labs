#q1
inventory = 0; 
total = 0
rejected_entries = 0

#q2
while True:
    stock_quantity = input("Please enter the stock quantity or type quit to exit")
    try:
       # q3
       stock_quantity = int(stock_quantity)
       #q6
       if stock_quantity > 0:
               total += int(stock_quantity) 
               print("current running total", total)
       #q5
       if stock_quantity < 0: 
            rejected_entries += 1
            print("Negative numbers are not allowed!")
       #q7
       if total > 500:
            print("The inventory has exceed 500 units!")
            break
    except:
        #q8
        if stock_quantity == "quit":
                            print(f"Total Units Processed:",total)
                            print(f"Number of failed/rejected entries", rejected_entries)
                            break
        #q4
        if stock_quantity != stock_quantity.isdigit():
            rejected_entries += 1
            print("Invalid input! Please enter a integer")
        
     

    
    


def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''
    capacity_of_inventory = 2000    # maximum stock allowed to be held
    
    if current_day == 0: #first day 
        previous_day_sales = 0 #first day so no sales will have been made from the previous day
    else:
        previous_day_sales = inventory_records[-1][1] #     -1 indicates the previous day in the inventory records tuple and 1 indicates the position of the data in the tuple which in this case is sales.
        
    available_items -= previous_day_sales # subtracts the sales from previous day with the amount of items in stock ie 2000 - 100 = 1900
    
    #creating a if statement to find out if its the 7th day which means restock of the product
    
    if current_day % 7 == 0: # divides current day by 7 and if there is no remainder ie 0 then it will restock supply
        restock_items = capacity_of_inventory - available_items # calculates how much supply is needed
        
        if restock_items > 0 :
            #this is for if restock needed is more than 0 it will add the restocked items to the available
            available_items += restock_items
            inventory_records.append((current_day, previous_day_sales,restock_items,available_items)) # adding all new details to the variable so the list can be updated for next day
        else:
            #for when inventory is full
            inventory_records.append((current_day,previous_day_sales,0,available_items))
    else:
        #this refers to the main if statement where if the current_day isnt divisable by 7 then it does restock
        inventory_records.append((current_day,previous_day_sales,0,available_items))
        
    
        
        

    return available_items

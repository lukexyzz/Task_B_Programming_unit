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
        previous_day_sales = inventory_records[-1][1] #    -1 indicates the previous day in the inventory records tuple and 1 indicates the position of the data in the tuple which in this case is sales.
        
        

    return available_items

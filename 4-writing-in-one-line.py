

# -------------------------------
# if conditional statement
# -------------------------------

meals = [
    
    {'hour': 8, 'food': "Barbari Bread"},
    {'hour': 8, 'food': "White Cheese"},

    {'hour': 12, 'food': "Pasta"},
    {'hour': 12, 'food': "Coca Cola"},

    {'hour': 21, 'food': "Bread"},
    {'hour': 21, 'food': "Yogurt"},
] 



print('------------------------------------------------------------------')

# 
for meal in meals:

    #   
    if (meal['hour'] < 12): time = 'breakfast'  
    if (meal['hour'] == 12): time = 'lunch'  
    if (meal['hour'] > 12): time = 'dinner'
    
    # 
    print('I ate ' + meal['food'] + ' as ' + time )

print('------------------------------------------------------------------')

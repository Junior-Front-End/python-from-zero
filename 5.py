

# -------------------------------
# switch conditional statement
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
    match meal['hour']:
        case 8:
            time = 'breakfast' 
        case 12:
            time = 'lunch' 
        case 21:
            time = 'dinner'
    
    # 
    print('I ate ' + meal['food'] + ' as ' + time )

print('------------------------------------------------------------------')

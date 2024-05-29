

# -------------------------------
# loop 
# -------------------------------

meals = [
    
    {'hour': '8 am', 'food': "Barbari Bread"},
    {'hour': '8 am', 'food': "White Cheese"},

    {'hour': '12 pm', 'food': "Pasta"},
    {'hour': '12 pm', 'food': "Coca Cola"},

    {'hour': '9 pm', 'food': "Bread"},
    {'hour': '9 pm', 'food': "Yogurt"},
] 



print('------------------------------------------------------------------')

for meal in meals:
    print('++ I ate ' + meal['food'] + ' in ' + meal['hour'] )

print('------------------------------------------------------------------')

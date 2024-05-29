

# -------------------------------
# function
# -------------------------------

meals = [
    {'hour': 8, 'food': "Barbari Bread"},
    {'hour': 8, 'food': "White Cheese"},
    {'hour': 12, 'food': "Pasta"},
    {'hour': 12, 'food': "Coca Cola"},
    {'hour': 21, 'food': "Bread"},
    {'hour': 21, 'food': "Yogurt"},
] 


# 
def getTime(hour){

    match hour:
        case 8: return 'breakfast' 
        case 12: return 'lunch' 
        case 21: return 'dinner'

}

print('------------------------------------------------------------------')

# 
for meal in meals:  
    print('I ate ' + meal['food'] + ' as ' + getTime(meal['hour']) )

print('------------------------------------------------------------------')

import random, datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
list_of_shops = [
    {'name': 'Tesco'},
    {'name': 'Asda'},
    {'name': 'Lidl'},
    {'name': "Sainsbury's"},
    {'name': 'Morrisons'},
    {'name': 'Aldi'},
    {'name': 'Waitrose'},
    {'name': 'Co-op'},
    {'name': 'Iceland'},
    {'name': 'Marks & Spencer'},
    {'name': 'Ocado'},
    {'name': 'Spar'},
    {'name': 'Nisa'},
    {'name': 'Budgens'},
    {'name': 'Farmfoods'},
    {'name': 'Poundland'},
    {'name': 'Home Bargains'},
    {'name': 'Booths'},
    {'name': 'Premier'},
    {'name': 'Tesco Express'},
    {'name': "Sainsbury's Local"},
    {'name': 'Co-op Food'},
    {'name': 'Londis'},
    {'name': 'Costco'},
    {'name': 'Whole Foods Market'},
    {'name': 'Poundstretcher'},
    {'name': 'B&M'},
    {'name': 'Superdrug'},
    {'name': 'Boots'}
]
list_of_items = [
    {'item': 'Carrots (1kg)',               'price': 0.91},
    {'item': 'Baking Soda (500g)',          'price': 5.15},
    {'item': 'Lotion (250ml)',              'price': 5.11},
    {'item': 'Whole Milk (2L)',             'price': 1.10},
    {'item': 'White Bread (800g)',          'price': 1.05},
    {'item': 'Eggs (12 pack)',              'price': 1.50},
    {'item': 'Chicken Breast (500g)',       'price': 3.75},
    {'item': 'Long Grain Rice (1kg)',       'price': 1.00},
    {'item': 'Spaghetti Pasta (500g)',      'price': 0.60},
    {'item': 'Apples (1kg)',                'price': 2.00},
    {'item': 'Bananas (1kg)',               'price': 1.20},
    {'item': 'Potatoes (2.5kg)',            'price': 2.50},
    {'item': 'Tomatoes (1kg)',              'price': 1.80},
    {'item': 'Cheddar Cheese (400g)',       'price': 2.20},
    {'item': 'Natural Yogurt (500g)',       'price': 1.25},
    {'item': 'Orange Juice (1L)',           'price': 1.20},
    {'item': 'Breakfast Cereal (500g)',     'price': 2.50},
    {'item': 'Butter (250g)',               'price': 1.80},
    {'item': 'Plain Flour (1kg)',           'price': 1.00},
    {'item': 'Granulated Sugar (1kg)',      'price': 0.75},
    {'item': 'Ground Coffee (200g)',        'price': 3.00},
    {'item': 'Tea Bags (80)',               'price': 2.00},
    {'item': 'Frozen Peas (1kg)',           'price': 1.20},
    {'item': 'Tinned Tomatoes (400g)',      'price': 0.50},
    {'item': 'Baked Beans (400g)',          'price': 0.60},
    {'item': 'Tuna Chunks (160g)',          'price': 0.70},
    {'item': 'Minced Beef (500g)',          'price': 4.00},
    {'item': 'Pork Sausages (6 pack)',      'price': 2.50},
    {'item': 'Back Bacon (250g)',           'price': 2.30},
    {'item': 'Rich Tea Biscuits (300g)',    'price': 1.20},
    {'item': 'Salted Crisps (150g)',        'price': 0.90},
    {'item': 'Chocolate Bar (45g)',         'price': 0.60},
    {'item': 'Toilet Roll (4 pack)',        'price': 1.50},
    {'item': 'Dishwashing Liquid (500ml)',  'price': 1.20},
    {'item': 'Shampoo (400ml)',             'price': 2.80},
    {'item': 'Handwash (300ml)',            'price': 1.50},
    {'item': 'Lavender Soap (100g)',        'price': 0.70},
    {'item': 'Laundry Detergent (1L)',      'price': 3.00},
    {'item': 'Aluminium Foil (20m)',        'price': 1.20},
    {'item': 'Batteries AA (4 pack)',       'price': 2.00},
    {'item': 'Black Pepper (100g)',         'price': 1.20},
    {'item': 'Sea Salt (500g)',             'price': 0.80},
    {'item': 'Olive Oil (500ml)',           'price': 3.00},
    {'item': 'Sunflower Oil (1L)',          'price': 1.50},
    {'item': 'White Vinegar (500ml)',       'price': 0.70},
    {'item': 'Soy Sauce (150ml)',           'price': 1.20},
    {'item': 'Ketchup (500g)',              'price': 1.00},
    {'item': 'Mayonnaise (430g)',           'price': 1.35},
    {'item': 'Mustard (200g)',              'price': 0.90},
    {'item': 'Peanut Butter (350g)',        'price': 1.50},
    {'item': 'Strawberry Jam (340g)',       'price': 1.10},
    {'item': 'Honey (340g)',                'price': 2.00},
    {'item': 'Orange Marmalade (340g)',     'price': 1.10},
    {'item': 'Breakfast Bars (6 pack)',     'price': 1.80},
    {'item': 'Muesli (750g)',               'price': 2.50},
    {'item': 'Rolled Oats (1kg)',           'price': 1.20},
    {'item': 'Cornflakes (500g)',           'price': 1.50},
    {'item': 'Grapes (500g)',               'price': 1.80},
    {'item': 'Strawberries (400g)',         'price': 2.00},
    {'item': 'Blueberries (150g)',          'price': 2.50},
    {'item': 'Raspberries (150g)',          'price': 2.50},
    {'item': 'Oranges (1kg)',               'price': 1.80},
    {'item': 'Lemons (4 pack)',             'price': 1.20},
    {'item': 'Limes (4 pack)',              'price': 1.20},
    {'item': 'Cucumbers (each)',            'price': 0.60},
    {'item': 'Lettuce (each)',              'price': 0.70},
    {'item': 'Broccoli (each)',             'price': 0.80},
    {'item': 'Cauliflower (each)',          'price': 1.00},
    {'item': 'Bell Peppers (3 pack)',       'price': 1.50},
    {'item': 'Mushrooms (300g)',            'price': 1.20},
    {'item': 'Onions (1kg)',                'price': 0.80},
    {'item': 'Garlic (3 bulbs)',            'price': 0.70},
    {'item': 'Ginger (100g)',               'price': 0.70},
    {'item': 'Cauliflower Rice (300g)',     'price': 1.30},
    {'item': 'Halloumi (200g)',             'price': 2.20},
    {'item': 'Tofu (300g)',                 'price': 1.50},
    {'item': 'Red Lentils (500g)',          'price': 1.00},
    {'item': 'Chickpeas (400g tin)',        'price': 0.55},
    {'item': 'Kidney Beans (400g tin)',     'price': 0.55},
    {'item': 'Brown Rice (1kg)',            'price': 1.50},
    {'item': 'Quinoa (500g)',               'price': 2.50},
    {'item': 'Tortilla Wraps (8)',          'price': 1.10},
    {'item': 'Pizza Base (fresh)',          'price': 1.00},
    {'item': 'Frozen Chips (1kg)',          'price': 1.50},
    {'item': 'Ice Cream (500ml)',           'price': 2.00},
    {'item': 'Fish Fingers (10)',           'price': 2.00},
    {'item': 'Chicken Nuggets (300g)',      'price': 2.00},
    {'item': 'Cocktail Sausages (400g)',    'price': 1.50},
    {'item': 'Cereal Bars (6 pack)',        'price': 1.80},
    {'item': 'Granola (500g)',              'price': 2.20},
    {'item': 'Breakfast Sausage (6 pack)',  'price': 1.80},
    {'item': 'Smoked Salmon (100g)',        'price': 3.00},
    {'item': 'Cream Cheese (200g)',         'price': 1.20},
    {'item': 'Double Cream (300ml)',        'price': 1.00},
    {'item': 'Crème Fraîche (200g)',        'price': 1.00},
    {'item': 'Ready Meal Lasagne (400g)',   'price': 2.50},
    {'item': 'Ready Meal Curry (400g)',     'price': 2.50},
    {'item': 'Frozen Pizza (classic)',      'price': 2.00},
    {'item': 'Energy Drink (330ml)',        'price': 1.20},
    {'item': 'Sparkling Water (1L)',        'price': 0.50},
]
#List of items to be shows on the receipt
purchased_items = []


#add a function that checks if the current item matches a value in the purchases_items list. it it does update the qty, if not add it
#as a new item

def check_and_update(item_to_check, item_number):
        item_found = False
        for current_item in purchased_items:
            if current_item['item'] == item_to_check:
                current_item['qty'] +=1
                current_item['total'] = round(float(current_item['price'] * current_item['qty']),2)
                
                # print(f"{current_item['item']} is already in the list")
                item_found = True
                break       
        # check_and_update(item_number)       
        if not item_found:
            purchased_items.append({'item': list_of_items[item_number]['item'],
                                    'price': list_of_items[item_number]['price'],
                                    'qty': 1, 'total':list_of_items[item_number]['price'] })


def get_list_of_items(number_of_items_purchased):
    # number_of_items_purchased = round(random.uniform(0,23))
    x = 0
    while x <= number_of_items_purchased:
        item_number = round(random.uniform(0,99))
        x += 1
        selected_item = list_of_items[item_number]['item']
        # print(f"Current Item: {selected_item}")
        check_and_update(selected_item, item_number)
    sum = 0
    print("-----Purchased Items-----")
    for item in purchased_items:
        if item['total'] > item['price']:
            print(f'{item["qty"]} -- {item["item"]} ------ £{item["total"]} (£{item["price"]} each)')
        else:
            print(f'{item["qty"]} -- {item["item"]} ------ £{item["price"]}')
        sum += float(item["price"])
        
   
def get_shop():
    shop_number = round(random.uniform(0,29))
    print("-----SHOP Information-----")
    shop_name = list_of_shops[shop_number]["name"]
    print(f'Name: {shop_name}')
    #  

def get_list_of_items_backup():
    purchased_items = []
    number_of_items_purchased = round(random.uniform(0,23))
    x = 0
    while x <=number_of_items_purchased:
        item_number = round(random.uniform(0,99))
        x += 1
        t = list_of_items[item_number]['item']

        print(f"Current Item: {t}")
        for current_item in purchased_items:
            if current_item['item'] == list_of_items[item_number]['item']:
                current_item.update({'qty': 2})
                print(f"{current_item['item']} is already in the list")
        
        
        purchased_items.append({'item': list_of_items[item_number]['item'],
                                'price': list_of_items[item_number]['price'],
                                'qty': 1})
        # purchased_items.append(list_of_items[item_numbers])
        print(purchased_items)
    # sum = 0
    print("-----Purchased Items-----")
    for item in purchased_items:
        print(f'{item["item"]} -- £{item["price"]}')
        # sum += float(item["price"])
        
    
    # print(x)
    # print(purchased_items)
   
    print("-----Payment Info-----")
    print(f'£{round(sum,2)}')
    print(f'Payment Method: Card ****{random.randrange(1111,9999)}')
    print("-------------------")
    
def sum_receipt_items():
    receipt_value = 0
    for item in purchased_items:
        receipt_value += float(item['price'])
    
    print(f"Total: £{round(float(receipt_value),2)}")

while True:
    try:
        custom_amount_of_items_check = int(input("Enter here: "))
        break
    except:
        print("Invalid")

if custom_amount_of_items_check:
    used_selected_amount = int(custom_amount_of_items_check) - 1
else:
    used_selected_amount = round(random.uniform(0,23))

get_shop()
print(f'Transaction ID: {random.randrange(19283,99999)}')
print(f'Date: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
get_list_of_items(used_selected_amount)
print("-----Payment Info-----")
sum_receipt_items()
print(f'Payment Method: Card ****{random.randrange(1111,9999)}')
print("-------------------")









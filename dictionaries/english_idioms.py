idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

space = " "
for key,values in idioms.items():
    print(key,":",space.join(values))

#print("Idioms", idioms)

my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    },
    "father": {
        "name": "Dwight",
        "age": 75
    }
}
for family_member, details in my_family.items():
    print(f'{details["name"]} is my {family_member} and is {str(details["age"])} years old')




stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
}

purchases = {}

purchases = [
    ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'EK', 200, '1-jul-1998', 56 )
]

total_stock = 0
stock_amount = 0

for (company_name, stock_number, date_of_purchase, stock_price) in purchases:
    stock_amount = stock_number*stock_price
    total_stock += stock_amount
    print(f"I purchased {stockDict[company_name]} for ${stock_amount} on {date_of_purchase}.")



for key in stockDict.keys():
    for (company_name, stock_amount, date_of_purchase, stock_price) in purchases:
        if company_name == key:
            print(f"{stock_amount} shares for {stock_price} dollars on {date_of_purchase}.")
            print(f"Total value of stock on portfolio: {total_stock}")




# for name in stockDict.items():
#     print(f"I purchased {name[1]} for {name2[1]*name2[3]} dollars")
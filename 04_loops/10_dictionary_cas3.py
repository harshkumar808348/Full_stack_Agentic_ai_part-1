users = [ 
    {"id":1 , "total":100 , "cupon":"p20"},
    {"id":2 , "total":200 , "cupon":"f10"},
    {"id":3 , "total":300 , "cupon":"p50"},
]

discounts = {
    "p20":(0.2 , 0),
    "f10":(0.5 , 0),
    "p50":(0, 10),
}

for user in users:
    precent, fixed = discounts.get(user["cupon"], (0, 0))
    discount_amount = user["total"] * precent + fixed
    print(f"{user['id']} paid {user['total']} and discount for next visit rupees {discount_amount}")
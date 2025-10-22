daily_sales= [5,10,12,7,3,8,9,15]
# figure out sales of  5 ruppes 

total_cups  = sum(sale for sale in daily_sales if sale>5)  # memory effecient operation

print(total_cups)

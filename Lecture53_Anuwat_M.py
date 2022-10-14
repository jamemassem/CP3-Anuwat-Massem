def vatcalculator(): 
    price = int(input('Please input your price : ')) 
    totalprice = price + (price*7)/100 
    return f'Totalprice = {totalprice}' 

print(vatcalculator())
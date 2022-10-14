def vatcalculator(price = int(input('Please input your price : '))): 
    return f'Totalprice = {price + (price*7)/100}' 

print(vatcalculator())
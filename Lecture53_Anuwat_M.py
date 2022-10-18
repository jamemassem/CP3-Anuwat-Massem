price = int(input('Please input your price : '))

def vatcalculator(price): 
    return f'Totalprice = {price + (price*7)/100}' 

print(vatcalculator(price))
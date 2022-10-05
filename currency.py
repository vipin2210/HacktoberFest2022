from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
print(from_currency, " To ", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print(result)

'''
Output:

Enter the amount: 56000
From Currency: USD
To Currency: INR
USD To INR 56000
4083923.247964
'''

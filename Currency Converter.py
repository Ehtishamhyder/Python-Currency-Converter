# currency converter
print("Welcome to the currency converter!")

def currency_converter(amt, from_currency, to_currency):
    price = {
        "USD": 1,
        "EUR": 0.84,
        "GBP": 0.73,
        "JPY": 153.0,
        "AUD": 1.40,
        "CAD": 1.35,
        "CHF": 0.76,
        "CNY": 7.2,
        "INR": 90.57,
        "PKR": 280.0,
        "SGD": 1.26,
        "SAR": 3.75,
        "AED": 3.67,
        "KRW": 1530.0,
        "MYR": 3.92,
        "LIRA": 43.61,
        "KWD": 0.31,
        "EGP": 46.85,
        "BDT": 122.2,
        "LKR": 309.17,

    }
     
    if from_currency not in price or to_currency not in price:
     print("Unsupported currency")
     return None
    
    # currency conversion
    amt_in_usd = amt / price[from_currency]
    converted_amt = amt_in_usd * price[to_currency]

    return converted_amt

print("Supported currencies: (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, INR, PKR, SGD, SAR, AED, KRW, MYR, LIRA, KWD, EGP, BDT, LKR)")
amt = float(input("Enter the amount you want to convert: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()

result = currency_converter(amt, from_currency, to_currency)
if result is not None:
    print(f"{amt} {from_currency} is equal to {result:.2f} {to_currency}")
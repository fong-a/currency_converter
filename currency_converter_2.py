# live currency converter
# uses the third party library: https://pypi.org/project/CurrencyConverter/

def converter(c, amount, convert_from, convert_to):
    result = c.convert(amount, convert_from, convert_to)
    return result

from currency_converter import CurrencyConverter
c = CurrencyConverter()
convert_from = input("Enter currency code, e.g. USD: ")
convert_to = input("Enter currency code, e.g. AUD: ")
amount = float(input("Enter the amount to convert: "))
print(converter(c, amount, convert_from, convert_to))



# Currency converter AUD - > USD

def convert(amount_to_convert, conversion_rate):
    if amount_to_convert <= 0:
        return "Error, please enter an amount over $0.00"
    return amount_to_convert * conversion_rate

conversion_rate = 0.69
amount_to_convert = float(input("Enter an amount"))
convert(conversion_rate, amount_to_convert)






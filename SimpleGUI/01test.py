value = 3.3333333333

# format to 1 decimal place
formatted_string = "{:.1f}".format(value)

print(formatted_string)



dollars = 4

# format to 2 decimal places (like money)
currency_format = "{:.2f}".format(dollars)

print(currency_format)

# convert to a number
currency_float = float(currency_format)

currency_float += float(formatted_string)

print(currency_float)

currency_floatFINAL = "{:.2f}".format(currency_float)

print(currency_floatFINAL)
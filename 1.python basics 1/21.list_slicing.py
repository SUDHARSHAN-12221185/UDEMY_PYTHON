amazon_cart=[
    'noteboook',
    'sunglassses',
    'toys',
    'grocery'
]

print(amazon_cart[0::2])

#lists are mutable
#everytimme we slice we shous consider that list to new list and we assign it to a variable
amazon_cart[0]='tablet'
print(amazon_cart)

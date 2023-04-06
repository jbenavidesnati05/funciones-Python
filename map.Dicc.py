items = [
    {
        "product":"camisa",
        "price":10,
    },
    {
        "product":"pantalones",
        "price":100,
    },
    {
        "product":"gorra",
        "price":20,
    }
]
print(items)
prices = list(map(lambda item : item["price"], items))
print(prices)

def agregarTaxes(item):
    item["taxes"] = item["price"]*0.19
    return item 

taxes = list(map(agregarTaxes,items))

print(taxes)
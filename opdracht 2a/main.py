import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
huwebshop = myclient["huwebshop"]
products = huwebshop["products"]

def vraag1():
    print("vraag 1:")
    first_product = products.find_one()
    print(first_product["name"], end=', ')
    print('€',first_product["price"]["selling_price"])

def vraag2():
    print("vraag 2:")
    for product in products.find():
        if product["name"][0] == 'R':
            print(product["name"])
            return

def vraag3():
    print("vraag 3:")
    totale_prijs = 0
    aantal_producten = 0
    for product in products.find():
        aantal_producten+=1
        totale_prijs += product["price"]["selling_price"]
    print(totale_prijs / aantal_producten)

vraag1()
vraag2()
vraag3()
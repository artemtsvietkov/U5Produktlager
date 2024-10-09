import csv
import os

db_file = 'db_products.csv'

def load_data():
    products = []
    if os.path.exists(db_file):
        with open(db_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if set(row.keys()) == {'id', 'name', 'desc', 'price', 'quantity'}:
                    products.append(row) 
    return products

def save_data(products):
    with open(db_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader() 
        for product in products:
            writer.writerow({field: product[field] for field in fieldnames})

def show_products():
    products = load_data() 
    if not products:
        print("Databasen är tom.")
    else:
        print("\nDatabasens innehåll:")
        for product in products:
            print(f"ID: {product['id']}, Namn: {product['name']}, Beskrivning: {product['desc']}, Pris: {product['price']}, Antal: {product['quantity']}")

def add_product():
    products = load_data() 
    new_id = input("Ange produktid: ")
    namn = input("Ange produktnamn: ")
    beskrivning = input("Ange produktbeskrivning: ")
    pris = input("Ange pris: ")
    antal = input("Ange antal: ")

    new_product = {
        'id': new_id,
        'name': namn,
        'desc': beskrivning,
        'price': pris,
        'quantity': antal
    }
    products.append(new_product)
    save_data(products)
    print("Produkten har lagts till.")

def remove_product():
    products = load_data() 
    id_to_remove = input("Ange ID på produkten du vill ta bort: ")
    products = [product for product in products if product['id'] != id_to_remove]
    save_data(products)
    print("Produkten har tagits bort.")

def meny():
    while True:
        print("\n1. Visa databasens innehåll")
        print("2. Lägg till produkt")
        print("3. Ta bort produkt")
        print("4. Avsluta")
        val = input("Välj ett alternativ: ")

        if val == '1':
            show_products()
        elif val == '2':
            add_product()
        elif val == '3':
            remove_product()
        elif val == '4':
            print("Programmet avslutas.")
            break
        else:
            print("Ogiltigt val, försök igen.")  

meny()

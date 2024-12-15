#In einem kleinen Sportartikelgeschäft werden Kundeninformationen aus geschäftlichen Gründen gespeichert. Zu den Kundeninformationen gehören Name, Telefonnummer, E-Mail und Adresse. Schreiben Sie eine kleine Software, die dem oben genannten Geschäft bei der Verwaltung von Kundeninformationen hilft. Die Software muss über einige der folgenden Funktionen verfügen:
#Zeigt Kundeninformationen an. Diese Informationen werden aus der Datei „customers.txt“ gelesen.
#Suche nach Kunden.
#Fügen Sie neue Kundeninformationen hinzu.
#Kundeninformationen aktualisieren.
#Kundeninformationen löschen.
#Speichern Sie die Änderungen in der Datei „customers.txt“.


import os

# File for customer information
FILENAME = 'customers.txt'

# Function to load customer information
def load_customers():
    customers = []
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            for line in file:
                name, phone, email, address = line.strip().split(',')
                customers.append({
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'address': address
                })
    return customers

def save_customers(customers):
    with open(FILENAME, 'w') as file:
        for customer in customers:
            file.write(f"{customer['name']},{customer['phone']},{customer['email']},{customer['address']}\n")

def display_customers(customers):
    if not customers:
        print("No customer information available.")
        return
    for customer in customers:
        print(f"Name: {customer['name']}, Phone: {customer['phone']}, Email: {customer['email']}, Address: {customer['address']}")

def search_customer(customers, name):
    for customer in customers:
        if customer['name'].lower() == name.lower():
            return customer
    return None

def add_customer(customers):
    name = input("Enter the customer's name: ")
    phone = input("Enter the customer's phone number: ")
    email = input("Enter the customer's email: ")
    address = input("Enter the customer's address: ")
    
    customers.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print("Customer added successfully.")

def update_customer(customers):
    name = input("Enter the name of the customer you want to update: ")
    customer = search_customer(customers, name)
    
    if customer:
        customer['phone'] = input("Enter the new phone number: ")
        customer['email'] = input("Enter the new email: ")
        customer['address'] = input("Enter the new address: ")
        print("Customer information updated successfully.")
    else:
        print("Customer not found.")

def delete_customer(customers):
    name = input("Enter the name of the customer you want to delete: ")
    customer = search_customer(customers, name)
    
    if customer:
        customers.remove(customer)
        print("Customer deleted successfully.")
    else:
        print("Customer not found.")

def main():
    customers = load_customers()
    
    while True:
        print("\n--- Customer Management ---")
        print("1. Display customer information")
        print("2. Search for a customer")
        print("3. Add a new customer")
        print("4. Update customer information")
        print("5. Delete customer information")
        print("6. Save changes")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_customers(customers)
        elif choice == '2':
            name = input("Enter the customer's name: ")
            customer = search_customer(customers, name)
            if customer:
                print(f"Found customer: {customer}")
            else:
                print("Customer not found.")
        elif choice == '3':
            add_customer(customers)
        elif choice == '4':
            update_customer(customers)
        elif choice == '5':
            delete_customer(customers)
        elif choice == '6':
            save_customers(customers)
            print("Changes saved successfully.")
        elif choice == '7':
            save_customers(customers)
            print("Program exited.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



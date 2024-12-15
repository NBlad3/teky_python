def format_price(price):
    return '{:,.0f}'.format(price).replace(',', ' ')

def main():
    products = []
    
    while True:
        name = input("Enter a product name (or 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        if not name.strip():
            print("Product name cannot be empty. Please try again.")
            continue
        while True:
            try:
                price = float(input("Enter the price of the product (in €): "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the price.")
        
        products.append((name, price))
    
    with open('sale_price.txt', 'a') as file:
        for name, price in products:
            sale_price = price * 0.9
            file.write(f"{name}, {format_price(price)}, {format_price(sale_price)}\n")

    print("The information has been saved in the file \"sale_price.txt\".")

if __name__ == "__main__":
    main()
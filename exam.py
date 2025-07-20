class Product:
    def __init__(self, code: str, name: str, description: str, quantity: int, price: float):
        self.code = code
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
    
    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'description': self.description,
            'quantity': self.quantity,
            'price': self.price
        }

    def add_product(self, product: Product):
        if self._find_product_by_code(product.code) is not None:
            return False
        self.products.append(product)
        return True
    
    def update_product(self, code: str, **updates):
        product = self._find_product_by_code(code)
        if product is None:
            return False
        
        for key, value in updates.items():
            if hasattr(product, key) and value is not None:
                setattr(product, key, value)
        return True
    
    def delete_product(self, code: str):
        product = self._find_product_by_code(code)
        if product is None:
            return False
        
        self.products.remove(product)
        return True
    
    def get_product(self, code: str):
        return self._find_product_by_code(code)
    
    def list_products(self):
        return self.products
    
    def sort_products(self):
        if not self.products:
            return
            
        valid_fields = ['code', 'name', 'price']
        if by not in valid_fields:
            by = 'code'
    
    def find_most_expensive(self):
        if not self.products:
            return None
        return max(self.products, key=lambda p: p.price)
    
    def _find_product_by_code(self, code: str):
        for product in self.products:
            if product.code.lower() == code.lower():
                return product
        return None
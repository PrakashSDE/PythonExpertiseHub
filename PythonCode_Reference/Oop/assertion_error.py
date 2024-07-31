class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        assert price > 0, f"Price{price}should be greater than 0"
        assert quantity > 0, f"Quantity{quantity} should be greater than 0"
    def calculate_total_price(self):
            return self.price * self.quantity

item1 = Item("Apple", -25, -3)

print(item1.calculate_total_price())

item2 = Item("Banana", 9, 20)

print(item2.calculate_total_price())

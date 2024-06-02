#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:  
            self.xxx = (self.discount / 100) * self.total
            self.total = self.total - self.xxx
            print (f"After the discount, the total comes to ${int(self.total)}.")
        
    
    def void_last_transaction(self):
        self.total -= self.last_transaction
        return len(self.items)
        
            

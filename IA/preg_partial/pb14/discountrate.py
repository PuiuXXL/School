class DiscountRate:
    def __init__(self):
        self.service_discounts = {
            "Premium" : 0.20,
            "Gold" : 0.15,
            "Silver" : 0.10 
        } 
        self.products_discount = {
            "Premium" : 0.10,
            "Gold" : 0.10,
            "Silver" : 0.10
        }
    def get_service_discount(self,member_type):
        return self.service_discounts.get(member_type,0)

    def get_product_discount(self,member_type):
        return self.products_discount.get(member_type,0)

    def set_service_discount(self, member_type, rate):
        self.service_discounts[member_type] = rate

    def set_products_discount(self, member_type, rate):
        self.products_discount[member_type] = rate
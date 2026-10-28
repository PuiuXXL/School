from customer import Customer
from discountrate import DiscountRate
from datetime import datetime

class Visit:
    def __init__(self,customer,date):
        self.customer = customer
        self.date = date
        self.service_expenses = 0
        self.product_expenses = 0

    def get_name(self):
        return self.customer.get_name()

    def get_service_expenses(self):
        return self.service_expenses

    def set_service_expenses(self,service_expenses):
        self.service_expenses = service_expenses

    def get_product_expenses(self):
        return self.product_expenses

    def set_product_expenses(self,product_expenses):
        self.product_expenses = product_expenses

    def get_total_expenses(self):
        discount = DiscountRate()

        member_type = None

        if self.customer.is_member():
            member_type = self.customer.get_member_type()

        service_rate = discount.get_service_discount(member_type)
        product_rate = discount.get_product_discount(member_type)

        services =  self.service_expenses * (1 - service_rate)
        products = self.product_expenses * (1 - product_rate)

        return services + products

    def __str__(self):
        return f"Customer {self.customer.get_name()}, Date:{self.date}, Tolal expenses: {self.get_total_expenses()}"
    








from customer import Customer
from discountrate import DiscountRate
from visit import Visit
from datetime import datetime


def main():
    # Client Premium
    customer1 = Customer("Alex")
    customer1.set_member(True)
    customer1.set_member_type("Premium")

    visit1 = Visit(customer1, datetime.now())
    visit1.set_service_expenses(200)
    visit1.set_product_expenses(100)

    print(customer1)
    print(visit1)

    print("-----------------------")

    # Client Gold
    customer2 = Customer("Maria")
    customer2.set_member(True)
    customer2.set_member_type("Gold")

    visit2 = Visit(customer2, datetime.now())
    visit2.set_service_expenses(300)
    visit2.set_product_expenses(150)

    print(customer2)
    print(visit2)

    print("-----------------------")

    # Client fara abonament
    customer3 = Customer("Andrei")

    visit3 = Visit(customer3, datetime.now())
    visit3.set_service_expenses(200)
    visit3.set_product_expenses(100)

    print(customer3)
    print(visit3)


if __name__ == "__main__":
    main()

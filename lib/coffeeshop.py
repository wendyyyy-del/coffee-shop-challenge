class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("The name must be a string between 1 and 15 char.")

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


class Coffee:
    all_coffees = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            Coffee.all_coffees.append(self)
        else:
            raise ValueError("The coffee must be a string with at least 3 characters.")

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0


class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer object.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee object.")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

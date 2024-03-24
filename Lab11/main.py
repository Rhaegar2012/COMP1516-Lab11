# Author: Jose Tellez
from car import Car


def main():

    car1 = Car("Honda", "Civic", 2020, 15000.0, 20000.0)
    print(car1.get_details())
    print("First Car's Initial Profit is $%.2f USD" % car1.calc_profit_usd())
    car1.reduce_price_usd(1000.0)
    print("First Car's New Profit is $%.2f USD" % car1.calc_profit_usd())
    print("")
    car2 = Car("BMW", "M3", 2019, 30000.0, 50000.0)
    print(car2.get_details())
    print(f"Second Car's Initial Profit is $%.2f USD" % car2.calc_profit_usd())
    car2.reduce_price_usd(5000.50)
    print(f"Second Car's New Profit is $%.2f USD" % car2.calc_profit_usd())


if __name__ == "__main__":
    main()

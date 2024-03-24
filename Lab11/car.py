# Author: Jose Tellez
class Car:
    """
    Represents a car in a car lot
    """
    def __init__(self,make, model, year, cost, price_usd):
        """Initializes the car details"""
        self._make = make
        self._model = model
        self._year = year
        self._cost_usd = cost
        self._price_usd = price_usd

    def calc_profit_usd(self):
        """ Returns the projected profit in USD """
        return self._price_usd - self._cost_usd

    def get_details(self):
        """
        Returns formatted string with car details
        :return: formatted string
        """
        return f"{self._year} {self._make} {self._model} for sale for $%.2f USD" % self._price_usd

    def reduce_price_usd(self, reduction_usd):
        """
        Reduce  the price value by the reduction amount
        :param reduction_usd: Reduction amount in USD
        :return:None
        """
        self._price_usd -= reduction_usd


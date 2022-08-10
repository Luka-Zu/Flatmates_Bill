class Bill:
    """
    object that contains data about a bill:
     1. Total amount
     2. perood
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    object that represents a flatmate that pays a bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass


class PdfReport:
    """
    creates a PDF class that contains a data about
    the flatmates such as their names and how much
    they each have to pay
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass
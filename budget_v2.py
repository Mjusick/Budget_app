class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            amount_to_withdraw = -amount
            self.deposit(amount_to_withdraw, description)
            return True
        else:
            return False

    def get_balance(self):
        return sum([product["amount"] for product in self.ledger])

    def transfer(self, amount, target_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + target_category.name)
            target_category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        descr_length_limit = 23
        amount_length_limit = 7

        category_header = self.name.center(30, "*") + "\n"
        list_of_transactions = ""
        for product in self.ledger:
            list_of_transactions += product["description"][:descr_length_limit].ljust(descr_length_limit)
            list_of_transactions += str('{:.2f}'.format(product["amount"]))[:amount_length_limit].rjust(
                amount_length_limit) + "\n"
        list_of_transactions += "Total: " + str(self.get_balance())
        return category_header + list_of_transactions


def get_total_expenditure(categories):
    list_of_expenditures = [product["amount"] for category in categories for product in category.ledger if
                            product["amount"] < 0]
    return sum(list_of_expenditures)


def get_category_names(categories):
    names = [category.name for category in categories]
    return names


def get_expenditures(categories):
    expenditures = []
    for category in categories:
        expenditures.append(sum([product["amount"] for product in category.ledger if product["amount"] < 0]))
    return expenditures


def get_percent_of_expenditures(categories):
    percent_of_expenditures = []
    expenditures = get_expenditures(categories)
    for expend in expenditures:
        percent_points = (expend / get_total_expenditure(categories)) * 100
        percent_of_expenditures.append(percent_points)
    return percent_of_expenditures


def create_spend_chart(categories):
    names = get_category_names(categories)
    percent_of_expenditure = get_percent_of_expenditures(categories)

    chart_title = "Percentage spent by category\n"
    for perc_counter in range(100, -10, -10):
        percent_indicator = (str(perc_counter) + "|").rjust(4)
        chart_title += percent_indicator
        for percent in percent_of_expenditure:
            if percent >= perc_counter:
                chart_title += " o "
            else:
                chart_title += "   "
        chart_title += " \n"

    horizontal_line = len(percent_indicator) * " " + ("---" * len(categories)) + "-"
    chart_title += horizontal_line

    longest_name = max(names, key=len)
    for index in range(len(longest_name)):
        chart_title += "\n"
        chart_title += 5 * " "
        for name in names:
            if index < len(name):
                name_letter = name[index] + "  "
                chart_title += name_letter
            else:
                chart_title += "   "
    return chart_title

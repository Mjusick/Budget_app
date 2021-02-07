# This entrypoint file to be used in development. Start by reading README.md
import budget_v2

from unittest import main

food = budget_v2.Category("Food")
entertainment = budget_v2.Category("Entertainment")
business = budget_v2.Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
food.withdraw(2.50,"hotdog")
food.withdraw(10.00,"chips")
entertainment.withdraw(10.00, "circus")
entertainment.withdraw(15.00, "cinema")
business.withdraw(45.00,"microwave")
business.deposit(60.00, "microwave")
food.withdraw(6.00, "water")
actual = budget_v2.create_spend_chart([business, food, entertainment])


print(food)
print(entertainment)
print(business)


print(actual)

# # Run unit tests automatically
# main(module='test_module', exit=False)



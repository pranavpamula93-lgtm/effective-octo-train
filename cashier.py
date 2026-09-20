class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = input("How many full dollars?: ")
        half_dollars = input("How many half dollars?: ")
        quarters = input("How many quarters?: ")
        nickels = input("How many nickels?: ")
        return int(dollars) + 0.5 * int(half_dollars) + 0.25 * int(quarters) + 0.05 * int(nickels)

    def transaction_result(self, coins, cost):
        if coins >= cost:
            print("Here is your change: $" + str(coins - cost))
            return True
        else:
            print("Sorry, the money you have given is not sufficient. Money refunded.")
            return False

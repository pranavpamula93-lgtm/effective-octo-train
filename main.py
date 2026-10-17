<<<<<<< HEAD
import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        option = input("What would you like? (small / medium / large / report / off): ")
        if option == "small" or option == "medium" or option == "large":
            if sandwich_maker_instance.check_resources(recipes[option]["ingredients"]):
                coins = cashier_instance.process_coins()
                if (cashier_instance.transaction_result(coins, recipes[option]["cost"])):
                    sandwich_maker_instance.make_sandwich(option, recipes[option]["ingredients"])
        elif option == "report":
            print("Bread: " + str(resources["bread"]) + " slice(s)")
            print("Ham: " + str(resources["ham"]) + " slice(s)")
            print("Cheese: " + str(resources["cheese"]) + " pound(s)")
        elif option == "off":
            break
        else:
            print("Invalid option. Please try again.")

if __name__=="__main__":
    main()
=======
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
>>>>>>> efc3756 (feat: added GET endpoints.)

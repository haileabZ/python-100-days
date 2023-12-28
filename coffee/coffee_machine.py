
import sys
Menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18
                }
            },
     "latte":{
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150
                }
            },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "coffee":24,
            "milk":100
            }
          }
         }

resources={
    "water":300,
    "milk":200,
    "coffee":100
}
money=0

def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}$")



def pay():
    print("Please enter coin!")
    total=int(input("How many quarters?: ")) * 0.25
    total+=int(input("How many dimes?: ")) * 0.1
    total+=int(input("How many nickles?: ")) * 0.05
    total+=int(input("How many pennies?: ")) * 0.01
    return total


def latte():
    global money
    if (resources["water"] >= 200 and resources["coffee"] >=24) and\
            resources["milk"] >= 150:
        response= pay()
        if response >= 1.5:
            money += 1.5
            change= response - 1.5
            resources["water"] -= Menu["latte"]["ingredients"]["water"]
            resources["coffee"] -= Menu["latte"]["ingredients"]["coffee"]
            resources["milk"] -= Menu["latte"]["ingredients"]["milk"]
            print(f"Here your change{change}")
            print("Here you have your latte!")
        else:
            print("The machine don't have enough money")
    else:
        print("you don't have enough resource")

def espresso():
    global money
    if resources["water"] >= 50 and resources["coffee"] >= 18:
        response = pay()
        if response >= 2.5:
            change = response - 2.5
            money += 2.5
            resources["water"] -= Menu["espresso"]["ingredients"]["water"]
            resources["coffee"] -= Menu["espresso"]["ingredients"]["coffee"]
            print(f"Here your change{change}")
            print("Here you have your espresso!")
        else:
            print("you don't have enough money")
    else:
        print("The machine don't have enough money")
def cappuccino():
    global money
    if (resources["water"] >= 250 and resources["coffee"] >= 24) \
            and resources["milk"] >= 100:
        response = pay()
        if response >= 3.0:
            money += 3.0
            change = response - 3.0
            resources["water"] -= Menu["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= Menu["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= Menu["cappuccino"]["ingredients"]["milk"]
            print(f"Here your change{change}")
            print("Here you have your cappuccino!")
        else:
            print("you don't have enough money")
    else:
        print("The machine don't have enough money")


while True:
    prompt= input("what would you like? (espresso/latte/cappuccino): ").strip()
    if prompt == "off":
        sys.exit(0)
    elif prompt == "report":
       report()
    elif prompt == "latte":
        latte()
    elif prompt == "espresso":
        espresso()
    else:
        cappuccino()




















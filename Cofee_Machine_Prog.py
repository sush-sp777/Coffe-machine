from art import art
MENU={
    "espresso" :{
        "ingredients":{
            "water":50,
            "cofee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "cofee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "cofee":24, 
        },
        "cost":3.0,
    }
}
Resources={
    "water":300,
    "milk":200,
    "cofee":100,
}
print(art)
Profit=0

def calculate_price():
    tot=int(input("How many quarters?:"))*0.25
    tot+=int(input("How many dimes?:"))*0.1
    tot+=int(input("How many nickels?:"))*0.04
    tot+=int(input("How many pennies?:"))*0.01
    return tot

def is_resource_sufficient(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item]>= Resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True

def is_transaction_succesful(money_recived,drink_cost):
    if money_recived >= drink_cost:
        change=round(money_recived-drink_cost,2)
        print(f"here is your change of {change}$")
        global Profit
        Profit+=drink_cost
        return True
    else:
        print("sorry the money is not sufficient")
        return False
    
def make_cofee(drink_name,ordered_ingredients):
    for item in ordered_ingredients:
        Resources[item]-=ordered_ingredients[item]
    print(f"here is your drink {drink_name}.")



should_continue=True
while should_continue:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice=="off":
        should_continue=False
    elif choice=="report":
        print(f"water:{Resources["water"]}ml\nmilk:{Resources['milk']}ml\ncofee:{Resources['cofee']}gm\nmoney: {Profit}$")
    else:
        drink=MENU[choice]
        if (is_resource_sufficient(drink["ingredients"])):
            payment=calculate_price()
            if is_transaction_succesful(payment,drink['cost']):

                make_cofee(choice,drink['ingredients'])
        else:
            should_continue=False

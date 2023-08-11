def roll_call_dwarves(dwarves):
    count = 1
    for dwarf in dwarves:
        print(f'{count}. {dwarf}')
        count += 1

    
def summon_captain_planet(planeteer_calls):
    each_item_calls = []

    for call in planeteer_calls:
        each_item_calls.append(call.capitalize() + '!')

    return each_item_calls    
     
    

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False


def find_the_cheese(foods):
    cheeses = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in cheeses:
            return food
    return None    
    


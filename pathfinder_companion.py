import random


def die_roll(num_sides):
    roll = random.randint(1, int(num_sides))

    if roll == 20:
        return "Critical HIT!"
    elif roll == 1:
        return "Critical Fail!"
    else:
        return roll


print("Would you like to roll some dice?")
response = input()

while response.lower() == 'yes':
    print("How many sides?")
    num_sides = input()
    print(die_roll(num_sides))
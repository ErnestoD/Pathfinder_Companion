import random


# Dice Roll Function
def die_roll(die_sides, die_times):
    die_count = 0
    roll = 0

    # Multiple Dice
    if die_times == '1':
        roll = random.randint(1, int(die_sides))
    elif die_times > '1':
        while die_count != int(die_times):
            roll += random.randint(1, int(die_sides))
            die_count += 1
    # Need to fix for ZERO input
    else:
        return "empty hand...? \nGrab some dice and try again!"
    # Rolls for Critical Hit/Fails only on d20
    if die_sides == '20' and die_times == '1':
        if roll == 20:
            return '"Critical HIT!"'
        elif roll == 1:
            return '"Critical Fail!"'
        else:
            return str(roll)
    # Coin
    elif die_sides == '2' and die_times == '1':
        if roll == 1:
            return str(roll) + " " + '(Heads)'
        elif roll == 2:
            return str(roll) + " " + '(Tails)'
    else:
        return str(roll)


# Start of program
print("Would you like to roll some dice?")
response = input().lower()

if response == 'yes':
    while response != 0:
        print("How many sides?")
        response = input()
        if response > '0':
            print("How many times?")
            times = input()
            print("You rolled a " + die_roll(response, times))
        else:
            print("Would you like to quit?")
            response = input().lower()
            if response == 'yes':
                break
elif response.lower() == 'no':
    print("Well have fun... I guess...")
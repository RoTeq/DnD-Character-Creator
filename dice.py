import random

def dice(number:int = 1,sides:int = 20,drop:tuple[str,int]=(None,None)) -> int:
    rolls = []
    for z in range(number):
        rolls.append(random.randint(1,sides))
    match drop[0]:
        case 'max':
            num = 0
            for x in range(drop[1]):
                find = max(rolls)
                for y in range(len(rolls)):
                    if rolls[y] == find:
                        rolls.pop(y)
            for roll in rolls:
                num += roll
        case 'min':
            num = 0
            for x in range(drop[1]):
                find = min(rolls)
                for y in range(len(rolls)):
                    try:
                        if rolls[y] == find:
                            rolls.pop(y)
                    except:
                        pass
            for roll in rolls:
                num +=roll
        case _:
            num = 0
            for roll in rolls:
                num += roll
    return num

print()
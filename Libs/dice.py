#DnD Character Creator
#    Copyright (C) 2024  Jacob Feldman
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

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


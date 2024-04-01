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

from sys import path
modpath = path[0]
modpath = modpath.split(sep='\\')
modpath.pop(-1)
modpath.pop(-1)
modpath = '\\'.join(modpath)
#modpath = f"{modpath}\\Libs"
path[0] = modpath
from Libs import dnd5api
from Libs import dice
from Libs import spellbook

api = dnd5api.DnD5eAPI()

print("success!")
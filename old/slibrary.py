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

from spellbook import sb

library_open = True
while library_open == True:
    query = input("What is your command: ")
    query = query.lower()
    match query:
        case "help":
            print(f"""
Search: Search the spellbook for spells
List: List the Spellbook's content
Exit: Exit the library
""")        
        case "search":
            spell = input("What spell are you searching for?: ")
            print()
            sb.Details(spell)
        case "list":
            sb.list_all()
            print()
        case "exit":
            library_open = False
        case _:
            print("Please ask for help if needed")
            print()
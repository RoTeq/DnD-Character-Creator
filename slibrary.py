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
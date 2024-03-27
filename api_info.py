from dnd5api import DnD5eAPI

api = DnD5eAPI()

def to_file(filename,data):
    f = open(filename,'wt')
    f.write("")
    f.close()
    f = open(filename,'at')
    for x in data['results']:
        f.write(f"{x['name']}\n")
    f.close()


running = True
while running == True:
    cmd = input("command mode [query, store]: ")
    match cmd:
        case "query":
            querying = True
            while querying == True:
                request = input("location: ")
                if request == "exit":
                    querying = False
                else:
                    data = api.request(request)
                    if len(data) == 2:
                        data = data['results']
                        for x in data:
                            print(x)
                    else:
                        for x in data:
                            print(x)
        case "store":
            filename = input("filename?: ")
            request = input("location: ")
            data = api.request(request)
            to_file(filename,data)






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

import libref

api = libref.dnd5api.DnD5eAPI()

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






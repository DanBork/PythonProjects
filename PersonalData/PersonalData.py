# Daniel Borkowy - PersonalData
# 26.11.2024

import json


class PersonalData:
    def __init__(self, name, surname, address, zipcode, idnumber):  # class initialisation
        self.name = name
        self.surname = surname
        self.address = address
        self.zipcode = zipcode
        self.idnumber = idnumber

    def __str__(self):  # method defining how to print class in terminal
        return f"{self.name} {self.surname}\nAddress: {self.address}\n{self.zipcode}\n" \
               f"Personal ID Number: {self.idnumber}"

    def to_json(self):      # writing class fields to json
        jsonfile = json.dumps(self.__dict__)
        with open(f"{self.name}{self.surname}.json", "w") as outfile:
            outfile.write(jsonfile)

    def from_json(self):    # reading form json and updating data
        with open(f"{self.name}{self.surname}.json", "r") as file:
            data = json.load(file)
            self.name = data["name"]
            self.surname = data["surname"]
            self.address = data["address"]
            self.zipcode = data["zipcode"]
            self.idnumber = data["idnumber"]


p1 = PersonalData("John", "Doe", "Katowice, ul. Sokolska 26", "40-085", 22002200)    # example object
p1.to_json()
p1.from_json()
print(p1)

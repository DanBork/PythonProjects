from dataclasses import dataclass, asdict
import json


@dataclass
class PersonalData:
    name: str
    surname: str
    address: str
    zipcode: str
    idnumber: int

    def __str__(self):
        return f"{self.name} {self.surname}\nAddress: {self.address}\n{self.zipcode}\n" \
               f"Personal ID Number: {self.idnumber}"

    def to_json(self):
        jsonfile = json.dumps(asdict(self))
        with open(f"{self.name}{self.surname}.json", "w") as outfile:
            outfile.write(jsonfile)

    @classmethod
    def from_json(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return cls(**data)


# Example usage
p1 = PersonalData("Andrew", "Bagpipe", "Katowice, ul. Sokolska 26", "40-085", 21123443)
p1.to_json()
p2 = PersonalData.from_json("AndrewBagpipe.json")
print(p2)

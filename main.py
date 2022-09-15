import json

db = {
    345646: ("Petro", 27),
    546768: ("Slava", 33),
    123533: ("Max", 12),
    456465: ("Sergey", 43),
    123344: ("Sem", 76)
}

with open("sample.json", "w") as outfile:
    json.dump(db, outfile)
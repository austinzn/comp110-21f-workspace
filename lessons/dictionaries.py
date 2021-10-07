"""Demonstrations of dictionary capabilities."""


schools: dict[str, int]

schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal
print(schools)

#access a value by its key "lookup"
print(schools["UNC"])

#remove a key value pair by its key
schools.pop("Duke")

#test for existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)

schools = {}
print(schools)

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
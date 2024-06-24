capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

print(capitals.get("USA"))
print(capitals.get("Japan"))

capitals.update({"India": "Not Found"})
capitals.update({"USA": "Detroit"})
print(capitals)


# ------------

capitals.pop("China")
capitals.popitem()
capitals.clear
print(capitals)


# ------------

capitals = {
    "USA": "Detroit",
    "India": "New Delhi",
    "Russia": "Moscow"
}

print(capitals.keys())
print(capitals.values())

for key in capitals.keys():
    print(key)
for value in capitals.values():
    print(value)
for key, value in capitals.items():
    print(f"{key}: {value}")
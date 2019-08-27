# Using set() to create a set
languages = set()

# Using curly braces allows you to initialize the set with values
languages = { 'english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese' }

print(languages)

showroom = set()

showroom = {"911", "m3", "cressida", "250"}

print(len(showroom))

showroom.add("s2000")

showroom.add("m3")

print(showroom)

showroom.update(["922", "then", "add"])

print(showroom)

showroom.discard("s2000")
print(showroom)

junkyard = set()
junkyard = {"mitsubishi", "f150", "caveleer", "oldsmobile"}

show_room = set()
show_room = {"911", "supra", "nsx", "skyline", "m3"}

inter = show_room.intersection(showroom)
print(inter)

union = junkyard.union(show_room, showroom)

print(union)

union.discard("caveleer")

print(union)
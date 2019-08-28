zoo = ("tiger", "otter", "minkey", "bever", "rabbit")

print(zoo.index("otter"))

find_animal = "minkey"

if find_animal in zoo:
    find_animal == zoo
    print(find_animal)

print(zoo[1])
print(zoo[2])
print(zoo[4])

new_zoo = (zoo[0:4])

print(list(new_zoo))
#in order to add to and create a list
#you must make it an empty list
new_zoo = []
new_zoo.extend(["terry", "tomlin"])

print(tuple(new_zoo))


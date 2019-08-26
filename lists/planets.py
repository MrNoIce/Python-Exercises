import random

# my_randoms = list()
# for i in range(10):
#     my_randoms.append(random.randrange(1, 6, 1))

# print(my_randoms)

# for number in range(1,6):
#     if my_randoms.__contains__(number):
#         print(f"my_randons list contains {number}")
#     else:
#         print(f"my_randoms list doent contain {number}")







planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]

print(planet_list)

planet_list.pop()


# Function and variable names are snake case instead of camel case
def create_person(first_name, last_name, age, occupation):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "occupation": occupation,
    }

melissa = create_person("Melissa", "Bell", 25, "Software Developer")

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def ran(running_kids):
    for i in running_kids:
        for x in range(len(running_kids)):
            print(running_kids[x])


print(*running_kids[1], "went running")

def run(name):
    print(f"Run: {name} was a runnin fool!")
def swing(name):
    print(f"Swing: {name} was a swinging away")
def slide(name):
    print(f"Slide: {name} slid around all over the place")
def hide(name):
    print(f"Hide: {name} hid from everyone")

for names in running_kids:
    run(names)
for names in swinging_kids:
    swing(names)
for names in sliding_kids:
    slide(names)
for names in hiding_kids:
    hide(names)
def chickenMonkey_mine():
    for num in range(1,101):
        if num % 5 == 0 and num % 7 == 0:
            print(f"Chicken Monkey")

        elif num % 5 == 0:
            print(f"chicken")

        elif num % 7 == 0:
            print(f"monkey")

        else:
            print(num)
chickenMonkey_mine()

# def multiples(m, count):
#     for i in range(count):
#         print(i*m)

def chicken_monkey_run():
    range_to_100 = range(1, 100)
    for num in range_to_100:
        if num % 5 == 0 and num % 7 == 0:
            print("chickenMonkey")
        elif num % 5 == 0:
            print("Chicken")
        elif num % 7 == 0:
            print("Monkey")
        else:
            print(num)
chicken_monkey_run()
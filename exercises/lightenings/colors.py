



eye_colors = [
  {
    "color": "brown"
  },
  {
    "color": "green"
  },
  {
    "color": "amber"
  },
  {
    "color": "blue"
  },
  {
    "color": "amber"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "brown"
  },
  {
    "color": "purple"
  },
  {
    "color": "purple"
  },
  {
    "color": "blue"
  },
  {
    "color": "blue"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "amber"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "brown"
  },
  {
    "color": "amber"
  },
  {
    "color": "blue"
  },
  {
    "color": "blue"
  },
  {
    "color": "green"
  },
  {
    "color": "green"
  }
]

for eyes in eye_colors:
    for key,value in eyes.items():
        print(f'Key "{key}" = {value}')

unique_colors = set()

for color_dict in eye_colors:
    current_color = color_dict["color"]
    unique_colors.add(current_color)

print(unique_colors)

color_table = {}

for color_dict in eye_colors:
    current_color = color_dict["color"]

    if current_color not in color_table:
        color_table[current_color] = 1
    else:
        color_table[current_color] += 1
print(color_table)


Appliances = ("oven", "refrigerator", "coffee maker", "rice cooker")
# Add 3 indispensable appliances to this tuple
Appliances = (*Appliances, "Coffee Grinder", "Toaster", "Juicer")
print(Appliances)

Appliances += ("time", "linter")
print(Appliances)
#Create a new collection that contains the  unique color names in the list above
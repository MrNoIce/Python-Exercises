"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["incredible"] = "When the first smell of fall starts to roll in"
word_definitions["exciting"] = "The first noticable feelings of fall"
word_definitions["Fall"] = "Not the moment when you start to loose balance"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["incredible"])
print(word_definitions["Fall"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for i in word_definitions:
    print(f"The drfinition of {i} is {word_definitions[i]}")
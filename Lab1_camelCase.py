"""
Write a program that turns a sentence into camel case. The first word is lowercase,
the rest of the words have their initial letter capitalized, and all the words are
joined together. For example, with the input "fOnt proCESSOR and ParsER", your program
will output "fontProcessorAndParser".

Optional extra question: print a warning message if the input will not produce a valid
variable name. You don't need to be exhaustive in checking, but test for a few common issues,
such as starting with a number, or containing invalid characters such as # or + or ".  Or, would
it be easier to check that the name only contains valid characters?

Test your program with different example inputs, and comment your code.
"""

# Note to self: Use `re.sub()` to replace any `-` or `_` with a space, using the regexp `r"(_|-)+"`.
# Use `str.title()` to capitalize the first letter of each word and convert the rest to lowercase.
# Finally, use `str.replace()` to remove spaces between words.


# def camelcase(str):
#   return ''.join(word.capitalize() or '_' for word in string.split('_'))

# creating a function which will convert string to camelcase
def camelcase(list_words):
    converted = "".join(word[0].upper() + word[1:].lower() for word in list_words)
    return converted[0].lower() + converted[1:]

words = ["HELLO", "wELCOME", "tO", "pYTHON", "pROGRAMMING"]
print(camelcase(words))
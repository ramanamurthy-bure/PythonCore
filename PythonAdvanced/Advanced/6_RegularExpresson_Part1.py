# Regular Expression - Part1
# We already know we can search for substrings within a larger string with the in operator
# "dog" in "my dog is great" -> True
# This has severe limitations, we need to know the exact string,and need to perform additional operations
# _ to perform additional operations to account for capitalization and punctuation
# What if we only the pattern structure of the string we are looking for? Like an e-mail or phone number?

# Regular Expressions (regex) allow us to search for general patterns in text data!
# For example, a simple e-mail format can be
#    user@email.com
# We know in this case we are looking for a pattern "text"+"@"+"text"+".com"
# The re library allows us to create specialized pattern strings and then search for matches within text
# The primary skill set for regex is understanding the special syntax for these pattern strings
# Phone No : (555)-555-5555
# Regex Pattern : r"(\d\d\d)-\d\d\d-\d\d\d\d"







"""
Cleaning Data.

You are given a list of user-entered social media usernames (handles). Your task is to clean and standardize this list to make all handles 

uniform and valid for a database. raw_handles = [ " @User123 ", " @john.doe_official ", "twitter@JaneSmith", "404-Error-Account", " @DATA_CLEANER_PRO ", " @PythonFanatic " ]

Data Cleaning Rules Your function must take the raw_handles list as input and return a new, cleaned list where every handle adheres to the following rules:

Leading/Trailing Whitespace: Remove any extra spaces from the beginning and end of the string. The '@' Symbol: Ensure the handle starts with a single '@' symbol.

If it has one, keep it. If it has extra characters (like 'twitter' or numbers) before the '@', or if it is missing the '@' entirely, it's an invalid handle and 

should be removed from the final list. Case Standardization: Convert the entire handle (after the '@') to lowercase.  Remove Invalid Characters: The valid handle name

 (the part after the '@') should only contain letters, numbers, and the underscore (_). Remove any hyphens (-) or periods (.) by replacing them with an underscore (_).

Remove Multiple Underscores: Ensure there are no multiple consecutive underscores (_) by replacing all occurrences with a single underscore (_).

"""

raw_handles =  [ " @User123  ", " @john.doe_official ", " twitter@JaneSmith", 
                "404-Error-Account", " @DATA_CLEANER_PRO ", " @Python-Fanatic ",
                "@blue-wall.", "@nEW-yORK.city" ]

def cleaning_data_strings(list1):

    raw_list = list1
    list_cleaned = []

    for index in raw_list:
        # Treatmeant : Removing extra spaces from the beginning and end of the string.
        word_treated = index.strip()

        # lowering word.
        word_treated = word_treated.lower()

        # replacing - and . with a underscore
        word_treated = word_treated.replace("-", "_").replace(".", "_")

        #if index.startswith("@"):
        if word_treated.startswith("@"):

            list_cleaned.append(word_treated)

    return list_cleaned

print(f'List cleaned is given by: {cleaning_data_strings(raw_handles)}')

        
        


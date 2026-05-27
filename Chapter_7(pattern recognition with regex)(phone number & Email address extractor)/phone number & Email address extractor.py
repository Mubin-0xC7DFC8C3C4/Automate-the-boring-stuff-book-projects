#! python 3.13.5
import pyperclip, re

phoneregex = re.compile(r'''(
    (\+\d{1,3})?                   # Optional country code
    (\s*)                          # Optional whitespace
    (\d{3}|\(\d{3}\))?             # Area code
    (\s|-|\.)?                     # Seperator
    (\d{3})                        # First 3 digits
    (\s|-|\.)?                     # Seperator
    (\d{4})                        # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # Optional extension
    )''',re.VERBOSE)

emailregex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+              # username
    @                              # symbol
    [a-zA-Z0-9.-]+                 # domain name
    (\.[a-zA-Z]{2,4})              # dot something
    )''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneregex.findall(text):
    matches.append(groups[0])

for groups in emailregex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')

print("The length of the list where phone number & Email addresses are added is: " + str(len(matches)))   # There's total 4000 dataset for Email and phone number. But there are some 
                                                                                                # null value in Email column. That's why the length of the list is less than 4000.
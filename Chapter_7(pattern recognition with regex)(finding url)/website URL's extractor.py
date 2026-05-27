#! python 3.13.5

import pyperclip, re

urlRegex = re.compile(r'https?://[\w.-]+(?:/[^\s]*)?', re.IGNORECASE)
text = str(pyperclip.paste())

matches = urlRegex.findall(text)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches)) 
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No website URL's(http:// or https://) found")
#! python 3.13.5

import re

urlRegex = re.compile(r'https?://[\w.-]+(?:/[^\s]*)?', re.IGNORECASE)
with open(r'C:\Users\HTC\python_code\Automate the boring stuff book project\Chapter_7(pattern recognition with regex)(finding url)\URL dataset.csv', encoding='utf-8') as content:
    text = content.read()
matches = urlRegex.findall(text)

if len(matches) > 0:
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No website URL's(http:// or https://) found")
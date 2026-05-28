#! python 3.13.5

import pyperclip, re

def standardize_date_format(date_str):
    match1 = re.match(r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', date_str)
    if match1:
        y, m, d = match1.groups()
        return f"{y}-{int(m):02d}-{int(d):02d}"

    match2 = re.match(r'(\d{1,2})[-/](\d{1,2})[-/](\d{4})', date_str)
    if match2:
        m, d, y = match2.groups()
        return f"{y}-{int(m):02d}-{int(d):02d}"

    return None 

text = pyperclip.paste()

date_pattern = r'\d{1,4}[-/]\d{1,2}[-/]\d{1,4}'
dates = re.findall(date_pattern, text)

standardized = [standardize_date_format(d) for d in dates if standardize_date_format(d)]

print(f"Cleaned and standard date format:\n{'\n'.join(standardized)}")
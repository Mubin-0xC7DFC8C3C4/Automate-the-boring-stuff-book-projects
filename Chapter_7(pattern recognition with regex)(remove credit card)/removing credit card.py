#! python 3.13.5

import re, pyperclip

text = pyperclip.paste()
credit_card_pattern = r'\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b'
print(re.sub(credit_card_pattern, "--------------------", text))

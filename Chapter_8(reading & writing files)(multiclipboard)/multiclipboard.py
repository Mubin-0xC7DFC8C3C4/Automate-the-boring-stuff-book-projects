#! python 3.13.5

import pyperclip, shelve, sys

mcbshelve = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelve.keys())))
    elif sys.argv[1] in mcbshelve:
        pyperclip.copy(mcbshelve[sys.argv[1]])

mcbshelve.close()
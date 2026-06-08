#! python 3.13.5

with open(r'C:\Users\HTC\python_code\Automate the boring stuff book project\Chapter_8(reading & writing files)(mad libs)\test.txt', 'r') as file:
    text = file.read()

placeholders = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']

for word in placeholders:
    while word in text:
        user_input = input(f"Enter a/an {word.lower()}: ")
        text = text.replace(word, user_input, 1)

print(text)

with open('print.txt', 'w') as output_file:
    output_file.write(text)
# paste used python terms 

glossary = {'integers': 'Are whole number datas.',
    'floats': 'Are numbers with decimal point.',
    'string concatenation': 'Joining two or more strings by using (+) or (,).',
    'list': 'Is a collection of iteams in a particular order.',
    'print': 'Is used to send message or output to the screen.',

# adding more 5 more phyton terms
    
    'boolean': 'Can be represented as true or false.',
    'variable': 'Stores a value by assigning it to a name.',
    'value': 'An item associated with a key in a dictionary.',
    'hashtag': 'To make a comment and indentation indicates a new line of code.',
    'dictionary': 'A collection of key-value pairs.' }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
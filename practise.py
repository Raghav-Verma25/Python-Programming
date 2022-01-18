"""example of nested dictionary comprehension"""

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

nd={k:('old' if v>40 else 'young') for (k,v) in original_dict.items()}
print(nd)

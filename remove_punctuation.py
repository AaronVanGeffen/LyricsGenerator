#! /usr/bin/env python3

import string


filename = "Project CCM/lyrics/Metal1000.txt"
raw_text = open(filename, encoding="utf8").read()
raw_text = raw_text.lower()

chars = sorted(list(set(raw_text)))
print(chars)

translator = str.maketrans('', '', "!\"#$&'()*,-./0123456789:;?[]_`{}")
no_punct = raw_text.translate(translator)
with open("Project CCM/lyrics/Metal1000 - no punctuation.txt", "w") as f:
	f.write(no_punct)

print(string.punctuation)

chars = sorted(list(set(no_punct)))
print(chars)
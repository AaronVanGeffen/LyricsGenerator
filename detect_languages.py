#!/usr/bin/env python3

from langdetect import detect
import os

for root, dirs, files in os.walk("./results/"):
	for file in files:
		if file == "genre.txt":
			continue

		with open(os.path.join(root, file), 'r') as handle:
			lyrics = handle.read()
			try:
				lang = detect(lyrics)
			except:
				lang = 'UNKNOWN'
			print(os.path.join(root, file), '->', lang)

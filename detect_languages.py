#!/usr/bin/env python3

from langdetect import detect
import os

for root, dirs, files in os.walk("./results/"):
	path = root.split(os.sep)
	print((len(path) - 1) * '-', os.path.basename(root))

	for file in files:
		with open(os.path.join(root, file), 'r') as handle:
			lyrics = handle.read()
			lang = detect(lyrics)
			print(len(path) * '-', file, '->', lang)

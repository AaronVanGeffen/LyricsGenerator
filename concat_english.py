#!/usr/bin/env python3

import csv
import os

with open('lyrics_eng.csv', 'w') as output: 
	writer = csv.writer(output)
	i = 0

	for line in open('languages_sorted_eng.txt', 'r'):
		filename = line.split(' -> ')[0]
		root = os.path.dirname(filename)
		title = os.path.basename(filename)
		year = os.path.basename(root)
		artist_dir = os.path.dirname(root)
		artist = os.path.basename(artist_dir)

		with open(os.path.join(artist_dir, "genre.txt"), 'r') as handle:
			genre = handle.read()
		
		with open(filename, 'r') as handle:
			lyrics = handle.read()

		writer.writerow([artist, year, title, genre, lyrics])
		i += 1

		if i % 1000 == 0:
			print(i)

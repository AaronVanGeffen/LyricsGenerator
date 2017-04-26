#!/usr/bin/env python3

import pandas as pd

pd.set_option('display.width', 120)

# Read CSV into data frame.
df = pd.read_csv("lyrics_start_end.csv", header = None, names = ['artist', 'year', 'title', 'genre', 'lyrics'])

# Write lyrics in text-files based on the first letter of the artist.
for index, row in df.iterrows():
	with open("lyrics/" + row['artist'][0] + ".txt", "a") as myfile:
		myfile.write(row['lyrics'])
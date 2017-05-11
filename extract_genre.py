#! /usr/bin/env python3

import pandas as pd
import numpy as np

genre = "Rock"

pd.set_option('display.width', 120)

# Read CSV into data frame.
df = pd.read_csv("lyrics_eng_skipped_5pct_non-ascii.csv", header = None, names = ['artist', 'year', 'title', 'genre', 'lyrics'])
print(df.shape)
df_genre = df[df['genre'] == genre]
print(df_genre.shape)

df_sample = df_genre.ix[np.random.choice(df_genre.index, 10000, replace=False)]
#print(df_sample)
print(df_sample.shape)

with open("lyrics/" + genre + ".txt", "a") as f:
	for index, row in df_sample.iterrows():
 			f.write("<S>\n" + row['lyrics'] + "\n<E>\n")
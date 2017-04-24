#!/usr/bin/env python3

import numpy as np
import pandas as pd

pd.set_option('display.width', 120)

# Read CSV into data frame.
df = pd.read_csv("lyrics_eng.csv", header = None, names = ['artist', 'year', 'title', 'genre', 'lyrics'])
df2 = df.ix[0:1000]

# Example: get row 5.
row = df.ix[5]

# Example: print genre from row above.
print(row['genre'])

# Add start and end token of lyric.
df.loc[:,'lyrics'] = "<S>" + df['lyrics'] + "<E>"
    
# Print lyric.
df.ix[0]['lyrics']

# Write to CSV.
df2.to_csv("lyrics_start_end.csv")   

#!/usr/bin/env python3

import numpy as np
import pandas as pd

pd.set_option('display.width', 120)

# Read CSV into data frame.
df = pd.read_csv("lyrics_eng.csv", header = None, names = ['artist', 'year', 'title', 'genre', 'lyrics'])

# Example: get row 5.
row = df.ix[5]

# Example: print genre from row above.
print(row['genre'])

#!/usr/bin/env python3

import numpy as np
import pandas as pd

pd.set_option('display.width', 120)

df = pd.read_csv("lyrics.csv")

# Drop empty lyrics
df = df[pd.notnull(df['lyrics'])]

# TODO: check for empty lyrics

# TODO: check for lyrics not containing \n

# TODO: merge with other dataset


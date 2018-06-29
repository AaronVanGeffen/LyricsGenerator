# -*- coding: utf-8 -*-
import argparse
from collections import Counter
import os


# Open file
def open_file(filename):
    with open (filename, 'r') as f:
        raw_text = f.read()

        return raw_text


### -------------
### MAIN FUNCTION
### -------------

def main():

    # Define directories
    src_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(src_dir, 'data/')

    # Set up argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("genre", help = "Choose the genre", choices = 
                        ["country", "metal", "pop"])

    args = parser.parse_args()
    genre = args.genre
    print("Genre:", genre)
    
    filename = genre + '1000.txt'
    lyrics = open_file(os.path.join(data_dir, filename)) # Read data from file
    print("Vocabulary size:", len(Counter(lyrics.split())))
    
### --------
### RUN CODE
### --------
        
if __name__ == "__main__":
    main()

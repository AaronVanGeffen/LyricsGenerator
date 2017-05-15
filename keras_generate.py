#!/usr/bin/env python3
import argparse
import os
import numpy
import sys
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# Parse arguments from command line.
parser = argparse.ArgumentParser(description='Train a neural network for lyric generation.')
parser.add_argument('--lyrics', dest='filename', required=True,
                    help='Dataset to use for training purposes')
parser.add_argument('--check', dest='checkpoint', required=True,
                    help='Checkpoint file to load weights from')

args = parser.parse_args()

# load ascii text and covert to lowercase
raw_text = open(args.filename).read()
raw_text = raw_text.lower()

# create mapping of unique chars to integers, and a reverse mapping
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

# summarize the loaded data
n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)

# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i:i + seq_length]
	seq_out = raw_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)

# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))

# normalize
X = X / float(n_vocab)

# one hot encode the output variable
y = np_utils.to_categorical(dataY)

# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))

# load the network weights
model.load_weights(args.checkpoint)
model.compile(loss='categorical_crossentropy', optimizer='adam')

def intListToString(pattern):
	return ''.join([int_to_char[value] for value in pattern])

def generateChars(pattern, N_chars=1000):
	out = pattern.copy()
	for i in range(N_chars):
		x = numpy.reshape(pattern, (1, len(pattern), 1))
		x = x / float(n_vocab)

		prediction = model.predict(x, verbose=0)
		index = numpy.argmax(prediction)
		# result = int_to_char[index]
		out.append(index)

		#seq_in = [int_to_char[value] for value in pattern]
		# sys.stdout.write(result)
		pattern.append(index)
		pattern = pattern[1:len(pattern)]

	print("===========")
	print(intListToString(out))
	print("===========")


# First, pick a random seed
start = numpy.random.randint(0, len(dataX)-1)
pattern = dataX[start]
print("Random seed:")
print("===========")
print(intListToString(pattern))
print("===========")

# Then, generate a random lyric...
generateChars(pattern)

# Finally, do the same for patterns from the user...
while len(pattern):
	print("Generate another lyric? Enter 100 chars, or leave blank to quit.")
	pattern = input("New pattern: ")

	# preprocess seed
	pattern = pattern.lower()
	pattern = [char_to_int[char] for char in pattern]

	if len(pattern):
		generateChars(pattern)

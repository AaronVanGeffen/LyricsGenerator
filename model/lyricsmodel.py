import numpy
import os
import sys

from keras.callbacks import ModelCheckpoint
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.models import Sequential
from keras.utils import np_utils

class LyricsModel:
	def __init__(self, options):
		self.options = options

		# load ascii text and covert to lowercase
		raw_text = open(self.options.trainingset).read()
		raw_text = raw_text.lower()

		# create mapping of unique chars to integers
		chars = sorted(list(set(raw_text)))
		self.char_to_int = dict((c, i) for i, c in enumerate(chars))
		self.int_to_char = dict((i, c) for i, c in enumerate(chars))

		# summarize the loaded data
		self.n_chars = len(raw_text)
		self.n_vocab = len(chars)
		print("Total Characters: ", self.n_chars)
		print("Total Vocab: ", self.n_vocab)

		# prepare the dataset of input to output pairs encoded as integers
		seq_length = 100
		self.dataX = []
		dataY = []
		for i in range(0, self.n_chars - seq_length, 1):
			seq_in = raw_text[i:i + seq_length]
			seq_out = raw_text[i + seq_length]
			self.dataX.append([self.char_to_int[char] for char in seq_in])
			dataY.append(self.char_to_int[seq_out])
			if i%100000==0:
				print("Now at:", i, "patterns")			

		self.n_patterns = len(self.dataX)
		print("Total Patterns: ", self.n_patterns)

		# reshape X to be [samples, time steps, features]
		print ("Reshaping: ", (self.n_patterns, seq_length, 1))
		X = numpy.reshape(self.dataX, (self.n_patterns, seq_length, 1))
		# normalize
		self.X = X / float(self.n_vocab)
		# one hot encode the output variable
		self.y = np_utils.to_categorical(dataY)

		self.loadModel()
		if self.options.checkpoint:
			self.loadWeights()
		self.compile()

	def loadModel(self, cellType=LSTM):
		# define the LSTM model
		self.model = Sequential()
		self.model.add(cellType(int(self.options.sequences), input_shape=(self.X.shape[1], self.X.shape[2]), return_sequences=(int(self.options.layers) > 1)))
		self.model.add(Dropout(float(self.options.dropoutRate)))

		for i in range(2, int(self.options.layers) + 1):
			isLastCell = i == int(self.options.layers)
			self.model.add(cellType(int(self.options.sequences), return_sequences=(not isLastCell)))
			self.model.add(Dropout(float(self.options.dropoutRate)))

		self.model.add(Dense(self.y.shape[1], activation='softmax'))

	def loadWeights(self):
		# load the network weights
		self.model.load_weights(self.options.checkpoint)

	def compile(self):
		self.model.compile(loss='categorical_crossentropy', optimizer='adam')

	def fit(self, initial_epoch=0):
		# check whether output directory exists -- create it if it doesn't.
		if not os.path.isdir(self.options.outdir):
			os.mkdir(self.options.outdir)

		# define the checkpoint
		filepath = os.path.join(self.options.outdir, "weights-improvement-{epoch:02d}-{loss:.4f}.hdf5")
		checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=False, mode='min')
		callbacks_list = [checkpoint]

		self.model.fit(self.X, self.y, epochs=50, batch_size=128, callbacks=callbacks_list, initial_epoch=initial_epoch)

	def intListToString(self, pattern):
		return ''.join([self.int_to_char[value] for value in pattern])

	def generateChars(self, pattern, n_char_gen=200):
		out = pattern.copy()
		for i in range(n_char_gen):
			x = numpy.reshape(pattern, (1, len(pattern), 1))
			x = x / float(self.n_vocab)

			prediction = self.model.predict(x, verbose=0)
			index = numpy.argmax(prediction)

			out.append(index)
			pattern.append(index)
			pattern = pattern[1:len(pattern)]
			sys.stdout.write(self.int_to_char[index])

		print("\n===========")
		print(self.intListToString(out))
		print("===========")

	def generateRandomString(self):
		# First, pick a random seed
		start = numpy.random.randint(0, len(self.dataX)-1)
		pattern = self.dataX[start]
		print("Random seed:")
		print("===========")
		print(self.intListToString(pattern))
		print("===========")

		# Then, generate a random lyric...
		self.generateChars(pattern)

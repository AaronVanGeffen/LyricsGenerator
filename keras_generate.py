#!/usr/bin/env python3
import argparse

from model import LyricsModel

# Parse arguments from command line.
parser = argparse.ArgumentParser(description='Generate lyrics using a trained neural network.')
parser.add_argument('--lyrics', dest='trainingset', required=True,
                    help='Dataset used to train the model')
parser.add_argument('--check', dest='checkpoint', required=True,
                    help='Checkpoint file to load weights from')
parser.add_argument('--nodes', dest='sequences', required=True,
                    help='Number of nodes per hidden layer')
parser.add_argument('--layers', dest='layers', required=True,
                    help='Number of hidden layers')
parser.add_argument('--dropout', dest='dropoutRate', required=True,
                    help='Dropout rate (as a proportion, e.g. 0.2)')

args = parser.parse_args()

model = LyricsModel(args)
model.generateRandomString()

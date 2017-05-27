#!/usr/bin/env python3
import argparse

from model import LyricsModel

# Parse arguments from command line.
parser = argparse.ArgumentParser(description='Generate lyrics using a trained neural network.')
parser.add_argument('--lyrics', dest='trainingset', required=True,
                    help='Dataset used to train the model')
parser.add_argument('--check', dest='checkpoint', required=True,
                    help='Checkpoint file to load weights from')

args = parser.parse_args()

model = LyricsModel(args)
model.generateRandomString()

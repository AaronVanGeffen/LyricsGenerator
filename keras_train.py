#!/usr/bin/env python3
import argparse

from model import LyricsModel

# Parse arguments from command line.
parser = argparse.ArgumentParser(description='Train a neural network for lyric generation.')
parser.add_argument('--lyrics', dest='trainingset', required=True,
                    help='Dataset to use for training purposes')
parser.add_argument('--check', dest='checkpoint', required=False,
                    help='Checkpoint file to load weights from')
parser.add_argument('--nodes', dest='sequences', required=True,
                    help='Number of nodes per hidden layer')
parser.add_argument('--layers', dest='layers', required=True,
                    help='Number of hidden layers')
parser.add_argument('--dropout', dest='dropoutRate', required=True,
                    help='Dropout rate (as a proportion, e.g. 0.2)')
parser.add_argument('--outdir', dest='outdir', required=True,
                    help='Folder to write weight files to')

args = parser.parse_args()

model = LyricsModel(args)
model.fit()

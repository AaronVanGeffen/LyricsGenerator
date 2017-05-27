#!/usr/bin/env python3
import argparse

from model import LyricsModel

# Parse arguments from command line.
parser = argparse.ArgumentParser(description='Train a neural network for lyric generation.')
parser.add_argument('--lyrics', dest='trainingset', required=True,
                    help='Dataset to use for training purposes')
parser.add_argument('--check', dest='checkpoint', required=False,
                    help='Checkpoint file to load weights from')
parser.add_argument('--outdir', dest='outdir', required=True,
                    help='Folder to write weight files to')

args = parser.parse_args()

model = LyricsModel(args)
model.fit()

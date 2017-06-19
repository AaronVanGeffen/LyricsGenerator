Generating lyrics using recurrent neural networks
=================================================

A project by Aaron van Geffen, Johanna de Vos, and Willem de Wit in the context of the Cognitive Computational Modelling of Web and Language course taught at the Radboud University Nijmegen.

This repository contains all Python files used in the gathering, training, and generation process as outlined in our paper. We will very briefly denote their purposes below.

Scraping
--------

Both `scrape_artists.py` and `scrape_lyrics.py` were used to scrape the MetroLyrics database, as the original [Kaggle dataset](https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics) did not meet expectations. We based these files on [the original scraping tools](https://github.com/h4ck3rk3y/lyrics_substance) used to generate the Kaggle dataset.

Preprocessing
-------------

`detect_languages.py` generates a report detailing what lyrics are considered English. `concat_english.py` then uses this report to concatenate these lyrics into a CSV.

`extract_genre.py` takes this CSV and splits it out by genre. As its name suggests, `remove_punctuation.py` was used to clean these CSVs even more.


Training and generation
-----------------------

Most importantly `keras_train.py` and `keras_generate.py` respectively train the model and generate lyrics through the generated weight files. To achieve this, they both make use of the `lyricsmodel.py` file, which instantiates Keras.

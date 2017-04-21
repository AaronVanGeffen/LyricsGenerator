#!/usr/bin/env python3
# Based on https://github.com/h4ck3rk3y/lyrics_substance/blob/master/artists.py
# (Modified to work with Python 3, amongst other things.)

import sys
import requests

from bs4 import BeautifulSoup

data = [chr(a) for a in range(ord('a'),ord('z')+1)]
data = ['1'] + data

output = open('artist.csv', 'a')

for alphabet in data:
	count = 1
	while True:
		link='http://www.metrolyrics.com/artists-%s-%d.html'%(alphabet,count)

		try:
			response = requests.get(link)
		except:
			print ('crashed at %s %d'%(alphabet, data))
			output.close()

		print ('trying %s' %(link) )

		if response.url != link:
			break

		soup =  BeautifulSoup(response.text, 'html.parser')

		for tr in soup.find_all('tr'):
			new_soup = BeautifulSoup(str(tr), 'html.parser')
			tds = new_soup.find_all('td')

			if not tds:
				continue
			else:
				artist_soup = BeautifulSoup(str(tds[0]), 'html.parser')
				genre_soup = BeautifulSoup(str(tds[1]), 'html.parser')

				artist_name = ''.join(artist_soup.a.contents).replace(' Lyrics', '')
				artist_link = artist_soup.a['href']
				genre = ' '.join(genre_soup.td.contents)

				if not genre:
					genre= 'Not Available'
				output.write('%s\t%s\t%s\n'%(artist_name,genre, artist_link))


		count+=1

output.close()

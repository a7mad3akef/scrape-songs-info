# import dependencies
import bs4 as bs
from urllib import urlopen
import datetime, time

## welcome message
print 'The system is running...'

# declare some needed variables
link = 'http://www.heart.co.uk/radio/last-played-songs/'
sauce = urlopen(link).read()
soup = bs.BeautifulSoup(sauce, 'lxml')


# fetch the specific tags
artists = soup.find_all('span', class_ = 'artist')
tracks = soup.find_all('span', class_ = 'track' )
stimes = soup.find_all('p', class_='publish_date' )


# filter the tag contains the track name
def filter_track(track):
	if(len(track.text.split('\n')) > 3):
		return track.text.split('\n')[3].split('        ')[-1]
	else:
		return track.text.split('\n')[1]


# filter the tag contains the artist name
def filter_artist(artist):
	if(len(artist.text.split('\n')) > 3):
		return artist.text.split('\n')[3].split('           ')[-1]
	else:
		return artist.text.split('\n')[1]

with open('data.csv','wb') as file:
	for i in range(len(stimes)):
		track = tracks[i+1]
		file.write(str(stimes[i].text.encode('utf8'))+','+str(filter_track(track).encode('utf8'))+','+str(filter_artist(artists[i+1]).encode('utf8')))
		file.write('\n')
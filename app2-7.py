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



while True:
	d = datetime.datetime.now().weekday()
	h = datetime.datetime.now().hour
	m = datetime.datetime.now().minute
	if ( d == 5 and h == 21 and m == 5 ):
		# writing the data to the file 
		print 'here'
		with open('saturday_data.csv','w') as file:
			for i in range(len(stimes)):
				track = tracks[i+1]
				file.write(str(stimes[i].text)+','+str(filter_track(track))+','+str(filter_artist(artists[i+1])))
				file.write('\n')
		time.sleep(59)
	if (d == 6 and h == 1 and m == 5):
		# writing the data to the file 
		print 'there'
		with open('sunday_data.csv','w') as file:
			for i in range(len(stimes)):
				track = tracks[i+1]
				file.write(str(stimes[i].text)+','+str(filter_track(track))+','+str(filter_artist(artists[i+1])))
				file.write('\n')
		time.sleep(59)
	time.sleep(1)




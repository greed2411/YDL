import subprocess
import os
import urllib.request
import urllib.error
import sys


"""
	YouTube Downloader used to download the best quality 
	audio, 
	video,
	Playlist of audio files,
	Playlist of video files
	from a URL belonging to https://www.youtube.com/
	
	Started working on : 21-06-2017
	
"""

def internet_on(url):

	try:

		urllib.request.urlopen(url, timeout=1)
		return True


	except urllib.error.URLError :

		print("Hmmm... you're not connected to the Internet")



def verify(url):
	
	if internet_on(url) == True:
		
		try :
			
			separation = url.split('/')
			print(separation[2])
			
			if separation[2] == 'www.youtube.com' or separation[2] == 'youtu.be':
				print('URL belongs to YouTube')		
				return True
		
		
		except Exception:
			
			print('Oops , Not a valid URL')
			sys.exit(1)


def main():
	
	try:
		
		choice = int(input('Enter \n1. Audio \n2. Video \n3. Audio Playlist \n4. Video Playlist\n'))
		url = str(input('Enter a valid URL from YouTube '))
		
		if verify(url) == True:
			
			if choice == 1:
				subprocess.call('youtube-dl -f 251 -o "/Audio downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)
				print('\n\nThe process is over and your file is probably residing in ' + os.getcwd() + '\\Audio downloads from youtube-dl' )
			
			elif choice == 2:
				subprocess.call('youtube-dl  -o "/Video downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --no-warnings "{url}"'.format(url=url), shell=True)
				print('\n\nThe process is over and your file is probably residing in ' + os.getcwd() + '\\Video downloads from youtube-dl' )
			
			elif choice == 3:
				subprocess.call('youtube-dl -i -o "%(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)
				print('\n\nThe process is over and currently residing in the current working directgory with the name of the folder same as that of playlist!')
			
			elif choice == 4:
				subprocess.call('youtube-dl -i -o "%(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --newline --no-warnings "{url}"'.format(url=url), shell=True)
				print('\n\nThe process is over and currently residing in the current working directgory with the name of the folder same as that of playlist!')	
	
	except IndexError:
		
		print('Not a URL') #not working
	
	except ValueError:
		
		print('You didn\'t enter a number! Shame on you!!')
			
	except Exception as e:
		
		print(e)
				
if __name__ == "__main__":
	
	main()


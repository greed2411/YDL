import subprocess
import os

url = input('Enter a valid URL from YouTube ')

try:
	choice = int(input('Enter 1. Video 2. Playlist of videos 3. Audio '))
	if choice == 1:
		subprocess.call('youtube-dl  -o "/Video downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --no-warnings "{url}"'.format(url=url), shell=True)
		print('The process is over and your file is probably residing in ' + os.getcwd() + 'Video downloads from youtube-dl' )
	elif choice == 3:
		subprocess.call('youtube-dl -f 251 -o "/Audio downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)
		print('The process is over and your file is probably residing in ' + os.getcwd() + 'Audio downloads from youtube-dl' )
		
except Exception as e:
			print(e)


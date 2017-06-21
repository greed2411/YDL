import subprocess
import os


"""
	YouTube Downloader used to download the best quality 
	video, 
	audio out of video,
	Playlist of video files,
	Playlist of audio files
	from a URL belonging to https://www.youtube.com/
	
	Started working on : 21-06-2017
	
"""


def video_link():
	return input('Enter a valid URL from YouTube ')


def playlist_link():
	return input('Enter a valid entire playlist link from YouTube ')


def main():
	
	try:
		
		choice = int(input('Enter \n1. Video \n2. Playlist of video files \n3. Audio \n4.Playlist of audio files\n'))
		
		if choice == 1:
			url = video_link()
			subprocess.call('youtube-dl  -o "/Video downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --no-warnings "{url}"'.format(url=url), shell=True)
			print('\n\nThe process is over and your file is probably residing in ' + os.getcwd() + '\\Video downloads from youtube-dl' )
			
		elif choice == 2:
			url = playlist_link()
			subprocess.call('youtube-dl -i -o "%(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --newline --no-warnings "{url}"'.format(url=url), shell=True)
			print('\n\nThe process is over and currently residing in the current working directgory with the name of the folder same as that of playlist!')
			
		elif choice == 3:
			url = video_link()
			subprocess.call('youtube-dl -f 251 -o "/Audio downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)
			print('\n\nThe process is over and your file is probably residing in ' + os.getcwd() + '\\Audio downloads from youtube-dl' )
		
		elif choice == 4:
			url = playlist_link()
			subprocess.call('youtube-dl -i -o "%(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)
			print('\n\nThe process is over and currently residing in the current working directgory with the name of the folder same as that of playlist!')
			
	except Exception as e:
				print(e)
				
if __name__ == "__main__":
	
	main()


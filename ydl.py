import subprocess
import os
import urllib.request
import urllib.error
import sys
import bs4


"""
	YouTube Downloader used to download the best quality 
	audio, 
	video,
	Playlist of audio files,
	Playlist of video files
	from a URL belonging to https://www.youtube.com/
	
	Started working on : 21-06-2017
	
"""

def internet_on():
	"""
		Checking whether connected to the internet 
		if not connected to internet but connected to wifi, not yet logged in, 
		returns a '200' code for trying to fetch results (wifi defualt login page)
	"""
	try:
		
		response = urllib.request.urlopen('http://google.com', timeout=1)
		soup = bs4.BeautifulSoup(response, 'lxml') 						 
		if soup.title.text == 'Google': 								  
		
			return True

	except (urllib.request.URLError, AttributeError) : #URLError if there is no internet or default wifi redirecting, AttributeError for handling 'Nonetype' object (response) in the above
		
		print("Hmmm... you're not connected to the Internet")
		sys.exit(1)
		



def verify(url):
	"""
		Verifying URL, whether it's a URL, whether that URL belongs to YouTube or not
	"""
	
	if internet_on() == True:
		
		try :
			
			separation = url.split('/')  
			
			if separation[2] == 'www.youtube.com' or separation[2] == 'youtu.be':
				
				"""
					Not checking whether URL is a playlist URL or not because of 
					YouTube's new User's 'My Mix' of songs, which don't have a 'playlist' in their URL
				"""
				
				print('URL belongs to YouTube')		
				return True
			
			else:
				
				print ("Not a YouTube URL") # test case : 'https://mail.google.com/mail/u/0/#inbox'
		
		except Exception:
			
			print('Oops , Not a valid URL') # test case : 'affdfsffasf'
			sys.exit(1)
	


def main():
	
	try:
		
		try:
			choice = int(input('Enter \n1. Audio \n2. Video \n3. Audio Playlist \n4. Video Playlist\n'))
			if choice not in [1, 2, 3, 4]:
				
				print("Enter a proper number from the choice, next time")	# test case : 5
				sys.exit(1)
			
		except:
			print('You didn\'t enter a proper number! Shame on you!!') # test case : 'dfsfsd'
			sys.exit(1)
			
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
				
			
	except Exception as e: #for any other unknown errors,  used it to get the other exceptions mentioned above
		
		print(e)
				
if __name__ == "__main__":
	
	main()


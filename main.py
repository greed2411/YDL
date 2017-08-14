from ydlcelery import audio, video, audio_playlist, video_playlist
import sys


def main():

        choice = int(input('Enter \n1. Audio \n2. Video \n3. Playlist of audio files\n4. Playlist of video files\n5.Quit the application\n'))
        if choice == 5:
                sys.exit(0)
        else:
                url = input('Enter a valid URL from YouTube ')

                if choice == 1:
                        audio.delay(url)
                elif choice == 2:
                        video.delay(url)
                elif choice == 3:
                        audio_playlist.delay(url)
                elif choice == 4:
                        video_playlist.delay(url)
                else:
                        pass


if __name__ == "__main__":

	main()
                        
                        




                        



          




                        



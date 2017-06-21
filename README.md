# YDL
## YouTube Downloader

A Python file to download Video(.mp4) and Audio(.mp3) Playlist of audio and video files just by providing the URL.

Tested and developed on ***Windows 7 32-bit SP1***

Yet to test on Ubuntu

### Command Line Programs Used
  * `youtube-dl` - Used to download the file from the internet
  * `ffmpeg` - Used for postprocess data, i.e., to convert file from .webm to .mp3 format
  
### Libraries used
  * [subprocess](https://docs.python.org/3/library/subprocess.html#older-high-level-api) - For running commands from python.
  * [os](https://docs.python.org/3/library/os.html) - to get the current working directory.
  
### Steps to follow
  * On Windows 
     1. Install `youtube-dl`
        
        ```youtube-dl installation
        pip install youtube-dl
        ```
        
        ```youtube-dl
        ```
### References
  * [wikiHow to Install FFmpeg on Windows](http://www.wikihow.com/Install-FFmpeg-on-Windows) - Helped me.
  * [Installing FFmpeg on all kind of environments](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
  * [extract audio with youtube-dl on windows](https://stackoverflow.com/a/42745019) - Hack for the [issue](https://github.com/NixOS/nixpkgs/issues/5236) 
  * [YouTube download using youtube-dl embedded with Python - 2017](http://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php) pretty useful summary of important stuff mentioned from [youtube-dl's documentation](https://github.com/rg3/youtube-dl)
  * [Improper documentation for Python](https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py) - You are all alone on the sea to understand the code and try if you want to use the package 'youtube_dl' , gave up trying to use the classes.
  
### Screenshots

![Youtube link of playlist for audio downloads URL](/../Jaiimmortal-wPlaylists/Audio_playlist.png?raw=true "0")

![Youtube link of playlist for audio downloads working](/../Jaiimmortal-wPlaylists/Audio_playlist(1).png?raw=true "1")

![Youtube link of playlist for audio downloads done](/../Jaiimmortal-wPlaylists/Audio_playlist(2).png?raw=true "2")

#### At the end of the day tried all four of 'em 

![End of the day 22-06-2017](/../Jaiimmortal-wPlaylists/EOD.png?raw=true "3")

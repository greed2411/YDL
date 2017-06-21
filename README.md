# YDL
##YouTube Downloader

A python file to download Video(.mp4) and Audio(.mp3) files just by providing the URL.

Tested and developed on ***Windows 7 32-bit SP1***
Yet to test on Ubuntu

### Command Line Programs Used:

  * [youtube-dl](https://github.com/rg3/youtube-dl) - Used to download the file from the internet
  * [ffmpeg](https://www.ffmpeg.org/ffmpeg.html) - Used for postprocess data, i.e., to convert file from .webm to .mp3 format
  
### Libraries used:
  * [subprocess](https://docs.python.org/3/library/subprocess.html#older-high-level-api) - For running commands from python.
  * [os](https://docs.python.org/3/library/os.html) - to get the current working directory.
  
### References
  * [wikiHow to Install FFmpeg on Windows](http://www.wikihow.com/Install-FFmpeg-on-Windows) - Helped me.
  * [Installing FFmpeg on all kind of environments](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
  * [extract audio with youtube-dl on windows](https://stackoverflow.com/a/42745019) - Hack for the [issue](https://github.com/NixOS/nixpkgs/issues/5236) 
  * [YouTube download using youtube-dl embedded with Python - 2017f](http://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php) pretty useful summary of important stuff mentioned from [youtube-dl's documentation](https://github.com/rg3/youtube-dl)
  * [Improper documentation for Python](https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py) - You are all alone on the sea to understand the code and try if you want to use the package 'youtube_dl' , gave up trying to use the classes.
  
  

  

# YDL
## YouTube Downloader (Synchronous)

A Python script to download Audio, Video and  Playlist of audio and video files just by providing the URL and get them at the best quality.

For ***Asynchrnous*** go [here](https://github.com/Jaiimmortal/YDL/tree/master/Async)

Tested and developed on ***Windows 7 32-bit SP1*** and ***Ubuntu GNOME 16.04 LTS*** and ***macOS Sierra 10.12.5***

### Command Line Programs Used
  * `youtube-dl` - Used to download the file from the internet
  * `ffmpeg` - Used for postprocess data, i.e., to convert file from .webm to .mp3 format
  
### Libraries used on Py 3.6.1 Anaconda, works with other py3 versions and distributions.
  * [subprocess](https://docs.python.org/3/library/subprocess.html#older-high-level-api) - For running commands from python.
  * [os](https://docs.python.org/3/library/os.html) - to get the current working directory.
  * [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) - For making GET methods
  * [urllib.error](https://docs.python.org/3/library/urllib.error.html#module-urllib.error) - For considering URLError
  * [sys](https://docs.python.org/3/library/sys.html) - For exiting out of the script
  * [bs4](http://beautiful-soup-4.readthedocs.io/en/latest/) - For scraping content while the user is connected to the internet or not, in case of wifi-connected , but not logged in
  * [lxml](http://lxml.de/#download) - For parsing the HTML document
  
  If you don't have either of the last two packages install them using,
  
  ```pip3 installation
  pip3 install bs4
  ```
  
  and 
  
  ```pip3 installation
  pip3 install lxml
  ```
  ***If you don't have pip3 or pip go [here](https://stackoverflow.com/a/6587528)***
  
### Steps to follow for installing dependencies
  * On Windows 
     1. Install `youtube-dl` via cmd
        
        ```youtube-dl installation
        pip install youtube-dl
        ```
     2. Install `ffmpeg` from [here](http://ffmpeg.zeranoe.com/builds/) and the [instructions](http://www.wikihow.com/Install-FFmpeg-on-Windows)
     
     3. And important thing : Move the contents of ffmpeg/bin/ to the location where `youtube-dl.py` is present as described in the [issue](https://stackoverflow.com/a/42745019)
     
     4. Run the script `ydl.py` via cmd
     
   * On Ubunutu or similar Distros
      1. Install `youtube-dl` via terminal
      
         ```youtube-dl installation
         pip install youtube-dl
         ```
      2. Install `ffmpeg`
      
         ```ffmpeg installation
         sudo apt-get install ffmpeg
         ```
      3. Run the scrpipt `ydl-ubuntu.py` in the terminal.
    
    * On macOS
      1. Install `youtube-dl` via terminal
         
            ```youtube-dl installation
         brew install youtube-dl
         ```
      2. Install `ffmpeg`
      
         ```ffmpeg installation
         brew install ffmpeg
         ```
      3. Run the scrpipt `ydl-ubuntu.py` in the terminal.
      
### References
  * [wikiHow to Install FFmpeg on Windows](http://www.wikihow.com/Install-FFmpeg-on-Windows) - Helped me.
  * [Installing FFmpeg on all kind of environments](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
  * [extract audio with youtube-dl on windows](https://stackoverflow.com/a/42745019) - Hack for the [issue](https://github.com/NixOS/nixpkgs/issues/5236) 
  * [YouTube download using youtube-dl embedded with Python - 2017](http://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php) pretty useful summary of important stuff mentioned from [youtube-dl's documentation](https://github.com/rg3/youtube-dl)
  * [Improper documentation for Python](https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py) - You are all alone on the sea to understand the code and try if you want to use the package 'youtube_dl' , gave up trying to use the classes.
  * for format conversion and extracting audio followed [this](http://www.slashgeek.net/2016/06/24/5-youtube-dl-tips-might-not-know/)
  
### Screenshots

![Youtube link of playlist for audio downloads URL](/../screenshots/1.png?raw=true "0")

![Youtube link of playlist for audio downloads working](/../screenshots/2.png?raw=true "1")

![Youtube link of playlist for audio downloads done](/../screenshots/3.png?raw=true "2")



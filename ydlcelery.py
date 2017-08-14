
# coding: utf-8

# In[4]:

import subprocess
from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def audio(url):
    subprocess.call('youtube-dl -f 251 -o "Audio downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)


@app.task
def video(url):
    subprocess.call('youtube-dl  -o "Video downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --no-warnings "{url}"'.format(url=url), shell=True)

@app.task
def audio_playlist(url):
    subprocess.call('youtube-dl -i -o "%(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" -q --yes-playlist --extract-audio --audio-format mp3 --no-warnings "{url}"'.format(url=url), shell=True)


@app.task
def video_playlist(url):
    subprocess.call('youtube-dl -i -o "%(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" -q --yes-playlist --newline --no-warnings "{url}"'.format(url=url), shell=True)

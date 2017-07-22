# YDL
## YouTube Downloader (Asynchronous)

A Python script to download Audio, Video and  Playlist of audio and video files just by providing the URL and get them at the best quality [Asynchronously](https://hackernoon.com/asynchronous-python-45df84b82434)

### Libraries used
  * [Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html) - Simple way to make Synchrnous tasks, Asynchronous.

### Installing the dependencies and getting started

  Please create a separate directory called `messaging` for this purpose 

  ```messaging
  mkdir ~/messaging
  cd ~/messaging
  ```

i. Install `celery`

  Celery is a task queue that is built on an asynchronous message passing system. It can be used as a bucket where programming tasks can be dumped. The program that passed the task can continue to execute and function responsively, and then later on, it can poll celery to see if the computation is complete and retrieve the data.

  ```pip installation
  pip install celery
  ```
  
 ii. Install `rabbitmq-server`
   
   ```
    sudo apt-get install rabbitmq-server
   ```
 
 iii. Start Celery Worker Processes
      
      celery worker -A ydlcelery &
     
  celery worker will get started , press `ctrl + C` to get back to the terminal.
      
 iv. Getting started

  Open terminal in the `messaging` directory and run `python main.py`
 
 v. To terminate the process at any time
 
     ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9
     
If you face any isssues refer to the actual Synchrnous version of this program [here](https://github.com/Jaiimmortal/YDL/blob/master/README.md)

### References

The most helpful article I came across while using Celery and RabbitMQ for Ubuntu machine, 
[How To Use Celery with RabbitMQ to Queue Tasks on an Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps)


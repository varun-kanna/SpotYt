# Setup
Use [exportify](https://watsonbox.github.io/exportify/) to convert the Spotify Playlists to CSV format.
Download the CSV's into the proper project folder. 
You should have the file path to the CSV, but preferably put it in the proper project folder. 
Now you should have at least one CSV playlist to use.
Then setup [ytmusicapi](https://ytmusicapi.readthedocs.io/en/latest/index.html) to create a browser.json file. 
Do the [Manual file creation](https://ytmusicapi.readthedocs.io/en/latest/setup/browser.html) and create a browser.json to use as the auth file.
You should now have a browser.json that you can use to pass in your information to the API.
If you followed the steps above, you should have main.py, browser.json, and a playlist csv.

# Running the script
`python -m venv venv`
`venv/Scripts/Activate.ps1` -> for powershell
`pip install ytmusicapi`

# Finding a playlist id from an existing youtube playlist
It's the alphanumeric sequence after `list=`

# An Example
Here we are using the Spotify Top 50 Global Songs Playlist as an example
![image](https://github.com/varun-kanna/Spotify-to-Youtube-Playlist-Converter/assets/73306137/bba877e7-8a36-43a3-9900-ad85e6834f90)

We enter the according details.
![image](https://github.com/varun-kanna/Spotify-to-Youtube-Playlist-Converter/assets/73306137/0d547c55-fb28-41b4-9413-00439d6e1bf2)

Then on YouTube Music we have the according playlist.
![image](https://github.com/varun-kanna/Spotify-to-Youtube-Playlist-Converter/assets/73306137/fbfb191f-a72e-4a1b-bf12-4c664f109dc4)

# Conclusion
The script may have errors when loading in the songs, but rerunning the script mutliple times will ensure all the songs are properly loaded.
If you have any suggestions or comments im open to feedback!

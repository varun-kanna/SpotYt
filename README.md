# spotify-to-youtube-playlist-converter
# Setup
Use exportify to convert the Spotify Playlists to CSV format.
Download the CSV's into the proper project folder. 
You should have the file path to the CSV, but preferably put it in the proper project folder. 
Now you should have at least one CSV playlist to use.
Then setup ytmusicapi to create a browser.json file. 
Do the "Manual file creation" and create a browser.json to use as the auth file.
You should now have a browser.json that you can use to pass in your information to the API.
If you followed the steps above, you should have main.py, browser.json, and a playlist csv.

# Running the script
`python -m venv venv`
`venv/Scripts/Activate.ps1` -> for powershell
`pip install ytmusicapi`

# Finding a playlist id from a youtube playlist
It's the alphanumeric sequence after `list=`

# An Example

# Conclusion
The script may have errors when loading in the songs, but rerunning the script mutliple times will ensure all the songs are properly loaded.
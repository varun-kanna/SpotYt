import csv
from ytmusicapi import YTMusic
import time 
def load_spotify_playlist(file):
    """Convert our spotify playlist to a list of songs"""
    songs = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        next(reader)
        for row in reader:
            #songs.append(f"{row[1]} lyrics {row[3]} ")
            songs.append(f"lyrics {row[1]} {row[3]}")
            #songs.append(f"{row[1]} {row[3]} lyrics {row[1]} {row[3]} ")
    return songs

def search_songs(ytmusic, searches):
    yt_video_ids = []
    for s in searches:
        result = ytmusic.search(s)
        try:
            vid = (result[0]["videoId"])
        except:
           vid = (result[1]["videoId"])
        yt_video_ids.append(vid)

    return yt_video_ids

if __name__ == "__main__":
    print("Connecting to YouTube Music...")
    ytmusic = YTMusic("browser.json")
    playlist_file = "vibes.csv"

    print("Loading exported Spotify playlist...")
    spotify_songs = load_spotify_playlist(playlist_file)

    print("Searching for songs on YouTube...")
    video_ids = search_songs(ytmusic, spotify_songs)
    
    print("Creating playlist...")
    try:
        res = ytmusic.search("VIBES", filter="playlists", scope="library")
        playlist_id = res[0]['browseId']
    except:
        playlist_id = ytmusic.create_playlist("VIBES", description="Some description")
    print("Adding songs...")

    for video_id in video_ids:
        print(video_id)
        #time.sleep(5) <- change if u wanna
        ytmusic.add_playlist_items(playlist_id, [video_id])
    print("Done!")
    
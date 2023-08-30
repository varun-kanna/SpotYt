import csv
from ytmusicapi import YTMusic

def options():
        """Choose between options to perform on playlists."""
        choice = input("\nPick a Spotify Playlist to convert to a Youtube PlayList or perform operation on existing YouTube Playlist.\n\
        Create a YouTube Playlist from a Spotify Playlist       - SPYT\n\
        Get an existing Playlist's details                      - ESP\n\
        Edit Playlist Title                                     - EPT\n\
        Edit Playlist Description                               - EPD\n\
        Edit Playlist Privacy Status                            - EPP\n\
        Delete an Existing Playlist                             - DP\n").upper().strip()
        if choice == 'SPYT':
            return 'spotify_to_youtube'
        elif choice == 'DP':
            return 'delete_playlist'
        elif choice == 'EPT':
            return 'edit_playlist_title'
        elif choice == 'EPD':
            return 'edit_playlist_description'
        elif choice == 'EPP':
            return 'edit_playlist_privacy'
        elif choice == 'ESP':
            return 'get_playlist_details'
    
def input_file():
    """Get the correct csv file from the user."""
    condition = True
    while condition:
        file = input("Please enter the filepath of the CSV: ")
        if file[-4:] == ".csv":
            return file
        else:
            print("Incorrect file path, try again")
        
def load_spotify_playlist(file):
    """Convert our spotify playlist to a list of songs."""
    songs = []
    with open(file, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        next(reader)
        for row in reader:
            songs.append(f"lyrics {row[1]} {row[3]}")
    return songs

def search_songs(ytmusic, searches):
    """Search for the songs and get their videoId's."""
    yt_video_ids = []
    for s in searches:
        result = ytmusic.search(s)
        try:
            vid = (result[0]["videoId"])
        except:
           vid = (result[1]["videoId"])
        yt_video_ids.append(vid)
    return yt_video_ids

def create_playlist(name, description, playlist_file):
    """Pass in the name for a playlist and add songs to playlist."""
    spotify_songs = load_spotify_playlist(playlist_file)
    video_ids = search_songs(ytmusic, spotify_songs)
    try:
        res = ytmusic.search(name, filter="playlists", scope="library")
        playlist_id = res[0]['browseId']
    except:
        playlist_id = ytmusic.create_playlist(name, description)
    for video_id in video_ids:
        #Ensures duplicates are not added.
        ytmusic.add_playlist_items(playlist_id, [video_id], duplicates=False)

def delete_playlist(playlistId):
    try:
        return ytmusic.delete_playlist(playlistId)
    except:
        print("Invalid PlaylistId")

def edit_playlist_title(playlistId, title):
    """Edit the title of a playlist."""
    try:
        return ytmusic.edit_playlist(playlistId=playlistId,title=title)
    except:
        print("Invalid PlaylistId")

def edit_playlist_description(playlistId, description):
    """Edit the description of a playlist."""
    try:
        return ytmusic.edit_playlist(playlistId=playlistId,description=description)
    except:
        print("Invalid PlaylistId")

def edit_playlist_privacy(playlistId, privacy):
    """Edit the privacy status of a playlist."""
    try:
        if not(privacy == "Public" or privacy == "Private"):
            print("Incorrect privacy answer.")
        else:
            return ytmusic.edit_playlist(playlistId=playlistId, privacyStatus=privacy)
    except:
        print("Invalid PlaylistId")

def get_playlist_details(playlistId):
    """Get the information of an existing playlist."""
    try:
        print(ytmusic.get_playlist(playlistId=playlistId, limit=None))
    except:
        print("Invalid PlaylistId")

if __name__ == "__main__":
    ytmusic = YTMusic("browser.json")
    option = options()
    if option == "spotify_to_youtube":
        name = input("Choose the name for the playlist: ")
        file = input_file()
        description = input("Choose the description for the playlist: ")
        create_playlist(name, description, file)
    elif option == "delete_playlist":
        playlistId = input("Please input the playlistId for the playlist you want to delete: ")
        delete_playlist(playlistId)
    elif option == "edit_playlist_title":
        playlistId = input("Please input the playlistId for the playlist you want to change the title for: ")
        name = input("Enter the new name for the playlist: ")
        edit_playlist_title(playlistId, name)
    elif option == "edit_playlist_description":
        playlistId = input("Please input the playlistId for the playlist you want to change the description for: ")
        description = input("Enter the new description for the playlist: ")
        edit_playlist_description(playlistId, description)
    elif option == "edit_playlist_privacy":
        playlistId = input("Please input the playlistId for the playlist you want to change the description for: ")
        privacy = input("Enter the new privacy for the playlist: 'Public' or 'Private': ")
        edit_playlist_privacy(playlistId, privacy)
    elif option == 'get_playlist_details':
        playlistId = input("Please input the playlistId for the playlist you want to get the details for: ")
        get_playlist_details(playlistId)
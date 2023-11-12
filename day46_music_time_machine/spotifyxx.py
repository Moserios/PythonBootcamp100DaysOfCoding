import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID =  "67bdfb212b5a4614bd2b75a25dc8e4ce"
SPOTIPY_CLIENT_SECRET = "ecaa8ad2adfb48b2ae3ce0bdb993740d"
REDIRECT_URL = "https://example.com"
SCOPE = "playlist-modify-private"

def spotify_part(song_list, custom_date): #

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URL,
                                                   scope=SCOPE))

    user_id = sp.current_user()["id"]

    track_list = []
    counter = 1
    for song in song_list[:100]:
        try:
            track_search = sp.search(q='track:' + song, type='track', limit=1)["tracks"]["items"][0]
            track_id = track_search["uri"]
            track_list.append(track_id)
            print(f"{counter}.{song}: {track_id}")
        except IndexError:
            print(f"{counter}.{song}: unavailable at Spotify")
        finally:
            counter += 1

    user_playlist_create_reply = sp.user_playlist_create(
        user_id,
        f"{str(custom_date)} Billboard 100 playlist",
        public=False,
        collaborative=False,
        description="Created with custom APP via APIs")

    new_playlist_id = user_playlist_create_reply["id"]

    sp.playlist_add_items(
       # user_id,
        playlist_id=new_playlist_id,
        items=track_list,
        position=None)


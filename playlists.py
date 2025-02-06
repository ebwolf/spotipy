import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

COUNTRY = 'DE'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

try:
    results = sp.current_user_saved_tracks()
    if results is None:
        print("No results")
    else:
        pprint.pprint(results)
except Exception as exc:
    print("Exception: ", exc)

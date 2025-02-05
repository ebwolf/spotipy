import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Pretty Lights'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']

if len(items) > 0:
    artist = items[0]
    print("Name: ", artist['name'])
    print("Followers: ", artist['followers']['total'])
    print("How to follow: ", artist['followers']['href'])
    print("Popularity: ", artist['popularity'])



aid = artist['id']
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(artist_id=aid, country="DE")

for track in results['tracks']:
    print('track    : ', track['name'])
    print('track ID : ', track['id'])


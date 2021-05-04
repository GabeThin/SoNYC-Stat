import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

SCOPE = 'user-library-read'
SPOTIPY_CLIENT_ID = 'f5eb6f7b95d84bd48dea9a50c1cca18f'
SPOTIPY_CLIENT_SECRET = '37a907df23374db5b9ac602f4847c2b4'
USERNAME = 'ssfvyd28qne3pasisps4exnlu'
REDIRECT_URI = 'http://localhost:5000'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

token = util.prompt_for_user_token(USERNAME, SCOPE, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, REDIRECT_URI)

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        # print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))
        print(i + 1, track['artists'][0]['name'], track['name'])

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(USERNAME)
    for playlist in playlists['items']:
            if playlist['owner']['id'] == USERNAME:
                print(playlist['name'])
                # print ('  total tracks', playlist['tracks']['total'])
                results = sp.playlist(playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from __future__ import print_function
import base64
import json
import requests
import sys

SPOTIFY_API_URL = 'https://api.spotify.com/v1'

CLIENT_ID = 'f5eb6f7b95d84bd48dea9a50c1cca18f'
CLIENT_SECRET = '37a907df23374db5b9ac602f4847c2b4'
# SPOTIPY_CLIENT_ID = 'f5eb6f7b95d84bd48dea9a50c1cca18f'
# SPOTIPY_CLIENT_SECRET = '37a907df23374db5b9ac602f4847c2b4'
USERNAME = 'ssfvyd28qne3pasisps4exnlu'
REDIRECT_URI = 'http://localhost:5000/home'

SCOPE = 'user-read-private user-read-email playlist-modify-public playlist-modify-private user-read-recently-played user-top-read user-library-read'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

token = util.prompt_for_user_token(USERNAME, SCOPE, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, REDIRECT_URI)

def show(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print(i + 1, track['artists'][0]['name'], track['name'])


if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(USERNAME)
    for playlist in playlists['items']:
            if playlist['owner']['id'] == USERNAME:
                print(playlist['name'])
                results = sp.playlist(playlist['id'], fields='tracks,next')
                tracks = results['tracks']

                print(playlists['items'])

                print()

                for item in sp.playlist_items(playlist['id'])['items']:
                    print(item['track']['name'])

                # print()
                # show(tracks)
                # while tracks['next']:
                #     tracks = sp.next(tracks)
                #     show(tracks)

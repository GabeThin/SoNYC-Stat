import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

client_id = 'f5eb6f7b95d84bd48dea9a50c1cca18f'
client_secret = '37a907df23374db5b9ac602f4847c2b4'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

ids = getTrackIDs('angelicadietzel', '4R0BZVh27NUJhHGLNitU08')

print(ids)

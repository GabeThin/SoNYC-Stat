from app import spotify
import math

class Album:
    def __init__(self, id):
        self.id = id
        self.tracks = []
    def format(self):
        data = spotify.album(self.id)
        self.title = data['name']
        self.artist = data['artists'][0]['name']
        self.image = data['images'][1]['url']
        for i in range(data['tracks']['total']):
            track = {}
            id = data['tracks']['items'][i]['id']
            track['name'] = data['tracks']['items'][i]['name']

            time = data['tracks']['items'][i]['duration_ms']
            minutes = math.floor((time/(1000*60))%60) + 1 if round((time/1000)%60) == 60 else math.floor((time/(1000*60))%60)
            seconds = round((time/1000)%60) - 60 if round((time/1000)%60) == 60 else round((time/1000)%60)
            track['length'] = str(minutes) + ':' + str(seconds) if len(str(seconds)) > 1 else str(minutes) + ':0' + str(seconds)

            track['popularity'] = spotify.track(id)['popularity']
            self.tracks.append(track)


class TopTracks:
    def __init__(self):
        self.names = []
        self.artists = []
        self.album_ids = []
        self.images = []
        self.ids = []
    def format(self):
        data = spotify.users_top_tracks()
        for i in range(0, 5):
            self.ids.append(data['items'][i]['album']['id'])
            self.names.append(data['items'][i]['name'])
            self.album_ids.append(data['items'][i]['album']['id'])
            self.artists.append(data['items'][i]['artists'][0]['name'])
            self.images.append(data['items'][i]['album']['images'][2]['url'])


class TopArtists:
    def __init__(self):
        self.names = []
        self.ids = []
        self.images = []
    def format(self):
        data = spotify.users_top_artists()
        for i in range(0, 5):
            self.images.append(data['items'][i]['images'][2]['url'])
            self.names.append(data['items'][i]['name'])
            self.ids.append(data['items'][i]['id'])


class RecentlyPlayed:
    def __init__(self):
        self.names = []
        self.artists = []
        self.album_ids = []
        self.images = []
        self.ids = []
    def format(self):
        data = spotify.users_recently_played()
        for i in range(0, 5):
            self.ids.append(data['items'][i]['track']['album']['id'])
            self.names.append(data['items'][i]['track']['name'])
            self.album_ids.append(data['items'][i]['track']['album']['id'])
            self.artists.append(data['items'][i]['track']['artists'][0]['name'])
            self.images.append(data['items'][i]['track']['album']['images'][2]['url'])

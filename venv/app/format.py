from app import spotify

class Album:
    def __init__(self, id):
        self.id = id
        self.tracks = []
        self.lengths = []
    def format(self):
        data = spotify.album(self.id)
        self.artist = data['artists'][0]['name']
        self.image = data['images'][1]
        for i in range(data['tracks']['total']):
            self.tracks.append(data['tracks']['items'][i]['name'])
            time = data['tracks']['items'][i]['duration_ms']
            seconds = round((time/1000)%60)
            minutes = round((time/(1000*60))%60)
            self.lengths.append(str(minutes) + ':' + str(seconds))


class TopTracks:
    def __init__(self):
        self.names = []
        self.artists = []
        self.albums = []
        self.images = []
        self.ids = []
    def format(self):
        data = spotify.users_top_tracks()
        for i in range(0, 5):
            self.ids.append(data['items'][i]['album']['id'])
            self.names.append(data['items'][i]['name'])
            self.albums.append(data['items'][i]['album']['name'])
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
        self.albums = []
        self.images = []
        self.ids = []
    def format(self):
        data = spotify.users_recently_played()
        for i in range(0, 5):
            self.ids.append(data['items'][i]['track']['album']['id'])
            self.names.append(data['items'][i]['track']['name'])
            self.albums.append(data['items'][i]['track']['album']['name'])
            self.artists.append(data['items'][i]['track']['artists'][0]['name'])
            self.images.append(data['items'][i]['track']['album']['images'][2]['url'])

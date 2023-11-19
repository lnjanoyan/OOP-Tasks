# hamarya done
import abc


class Song(abc.ABC):
    history = []

    def __init__(self, title: str, artist: str, length: str):
        self.title = title
        self.artist = artist
        self.length = length

    def listening(self):
        print(self.title, 'is listening')
        self.history.append(self.title)


class Album:
    def __init__(self, title: str, artist: str, date: str):
        self.title = title
        self.artist = artist
        self.date = date


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        if song in self.songs:
            print('Song already exists.')
        else:
            self.songs.append(song)

    def remove_song(self, song: Song):
        self.songs.remove(song)

    def display_playlist(self):
        for i in self.songs:
            print(self.name, '-', [i.title, i.artist, i.length])

    def search(self, song_name: str):
        for i in self.songs:
            if i.title == song_name:
                print(f'"{song_name}" song is present in "{self.name}" playlist. ')
                break
        else:
            print('Song not found!')

    def view_history(self):
        print('History - ', Song.history)


class Rock(Song):
    def __init__(self, title: str, artist: str, length: str):
        super().__init__(title, artist, length)


class Pop(Song):
    def __init__(self, title: str, artist: str, length: str):
        super().__init__(title, artist, length)


class MusicStreamingService(abc.ABC):
    def __init__(self, songs: list, albums: list, playlist: list):
        ...

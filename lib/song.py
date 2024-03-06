class Song:
    count = 0
    artists = []
    artist_count = {}
    genres = []
    genre_count = {}
    def __init__(self, name, artist, genre):
        
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()

        Song.add_to_artists(artist)
        Song.add_to_artist_count(artist)

        Song.add_to_genres(genre)
        Song.add_to_genre_count(genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1    

    @classmethod
    def add_to_artists(cls, artist):
        # Add new genre to the list if it's not already present
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_artist_count(cls, artist):
        # Increment the count for the artist
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1       

    @classmethod
    def add_to_genres(cls, genre):
       # Add new genre to the list if it's not already there
       if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increment the count for the genre
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

print(ninety_nine_problems.name)   
print(ninety_nine_problems.artist) 
print(ninety_nine_problems.genre)

print(Song.count) 
print(Song.genres) 
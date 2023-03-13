class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def liked(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f'{self._name} - Year: {self.year} - {self._likes} likes'


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self.name} - Year: {self.year} - Duration: {self.duration} min - {self.likes} likes'


class Show(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self.name} - Year: {self.year} - Seasons: {self.seasons} - {self.likes} likes'


class Playlist():
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    @property
    def listing(self):
        return self._programs

    def __len__(self):
        return len(self._programs)


psycho = Movie('psycho', 1960, 109)
vertigo = Movie('vertigo', 1958, 128)
fightclub = Movie('fight club', 1999, 139)
deadpool = Movie('deadpool', 2016, 108)
sopranos = Show('the sopranos', 1999, 6)
sharpobjects = Show('sharp objects', 2018, 1)
hunterxhunter = Show('hunter x hunter', 2011, 5)

psycho.liked()
vertigo.liked()
fightclub.liked()
fightclub.liked()
sopranos.liked()
sharpobjects.liked()
sharpobjects.liked()
hunterxhunter.liked()
hunterxhunter.liked()
deadpool.liked()
deadpool.liked()

movies_and_shows = [psycho, vertigo, fightclub, deadpool, sopranos, sharpobjects, hunterxhunter]
programs_playlist = Playlist('programs playlist', movies_and_shows)

print(f'Playlist size: {len(programs_playlist)} movies and/or shows')


for program in programs_playlist:
    print(program)

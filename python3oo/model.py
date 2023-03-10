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
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return f'{self._name} - Year: {self.year} - {self._likes} likes'


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self._name} - Year: {self.year} - Duration: {self.duration} min - {self._likes} likes'


class Show(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self._name} - Year: {self.year} - Seasons: {self.seasons} - {self._likes} likes'


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self.programs = programs

    def size(self):
        return len(self.programs)


psycho = Movie('psycho', 1960, 109)
vertigo = Movie('vertigo', 1958, 128)
fightclub =Movie('fight club', 1999, 139)
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

movies_and_shows = [psycho, vertigo, fightclub, sopranos, sharpobjects, hunterxhunter]
program_playlist = Playlist('programs playlist', program_playlist)

for program in program_playlist.programs:
    print(program)

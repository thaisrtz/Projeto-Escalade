class Movie:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def liked(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()


class Show:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def liked(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()


psycho = Movie('psycho', 1960, 109)
psycho.liked()
print(f'Name: {psycho.name} - Year: {psycho.year} - Duration: {psycho.duration} minutes - Likes: {psycho.likes}')


sopranos = Show('the sopranos', 1999, 6)
sopranos.liked()
sopranos.liked()
print(f'Name: {sopranos.name} - Year: {sopranos.year} - Seasons: {sopranos.seasons} - Likes: {sopranos.likes}')

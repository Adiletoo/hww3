class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name_hero(self):
        return f'Hero name ==> {self.name}'

    def extra_health(self):
        self.health_points *= 2
        return self.health_points

    def __str__(self):
        return f'{self.nickname} {self.superpower} {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Saitama', 'Bald cloak', 'Strongest', 999, 'heroism')
print(hero.name_hero())
print(hero.extra_health())
print(hero.__len__())
print(hero.__str__())
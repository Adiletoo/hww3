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
# print(hero.name_hero())
# print(hero.extra_health())
# print(hero.__len__())
# print(hero.__str__())



class FriendHero(SuperHero):
    fly = False
    damage = False
    kunai = True

    def extra_health(self):
        self.health_points **= 2
        FriendHero.fly = True
        return self.health_points

    def __str__(self):
        return f'fly in the True_phrase'


friend = FriendHero("King", 'Strongest Man of the planet', 'extreme luck', 50, 'I am the strongest')
print(friend.extra_health())
print(friend.fly)
print(friend.__str__())


class BrotherHero(SuperHero):
    fly = False
    damage = False
    sword = True

    def extra_health(self):
        self.health_points **= 2
        BrotherHero.fly = True
        return self.health_points

    def __str__(self):
        return f'fly in the True_phrase'


bro = BrotherHero('Genos', 'Kiborg', 'Flight', 666, 'my teacher is the strongest')
print(bro.extra_health())
print(BrotherHero.fly)
print(bro.__str__())


class Villain(BrotherHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2
        return self.damage


print(BrotherHero.damage)
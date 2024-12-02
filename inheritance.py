import Superhero


class AlienHero(Superhero):
    def __init__(self, name, power, weakness, planet):
        super().__init__(name, power, weakness)
        self.planet = planet

    def display_info(self):
        return f"Name: {self.name}, Power: {self.power}, Weakness: {self.weakness}, Planet: {self.planet}"

# Create an instance of AlienHero
alien_hero = AlienHero("Star Guardian", "Telepathy", "Kryptonite", "Mars")
print(alien_hero.display_info())
print(alien_hero.save_the_day())

class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.weakness = weakness

    def display_info(self):
        return f"Name: {self.name}, Power: {self.power}, Weakness: {self.weakness}"

    def save_the_day(self):
        return f"{self.name} uses {self.power} to save the day!"

# Create an instance
hero1 = Superhero("Wonder Light", "Invisibility", "Water")
print(hero1.display_info())
print(hero1.save_the_day())

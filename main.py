

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} attacked {other.name} for {self.attack_power} damage.")
    def is_alive(self):
        if self.health > 0:
            print(f"{self.name} has {self.health} health remaining.")
            return True
        else:
            print(f"{self.name} is dead.")
            return False

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if self.computer.is_alive():
                self.computer.attack(self.player)

Player1 = Hero("Player1")
Player2 = Hero("Player2")

Game = Game(Player1, Player2)
Game.start()

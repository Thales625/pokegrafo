class teste:
    def __init__(self, name):
        self.name = name

def __str__(self):
    return f"{self.name}"

viado = teste("Viado da bike")
print(viado)
print("olho do cu")

class Pokemon:
      def __init__(self, name, type, hp, attack, defense, moves):
            self.name = name
            self.type = type
            self.hp = hp
            self.attack = attack
            self.defense = defense
            self.moves = moves #use an array to show his moveset (python e op dms, em c eu teria que escapara da samsara pra fazer algo assim...acho que to me apaixonando)
      
      def __str__(self):
            return f"{self.name} (Tipo: {self.type} HP: {self.hp} Attack: {self.attack} Defense: {self.defense})"             
            
class Trainer:
      def __init__(self, name):
            self.name = name
            self.team = [] #array to arrange pokemons
            self.items = {"Pokeballs": 5, "Potion": 3} #initial inventory
            
      def catch_pokemon(self, pokemon):
            if len(self.team) < 6:
                  self.team.append(pokemon)
                  print(f"{self.name} has capture a {pokemon.name}")
            else:
                  print("you already have a full roster")
      
      def show_roster(self):
            if self.team:
                  print(f"{self.name} team:")
                  for pokemon in self.team:
                        print(f" | {pokemon}")
            else:
                  print(f"{self.name} doesnt have any pokemons yet...")
                  
      def use_item(self,item):
            if item in self.items and self.items[item] > 0:
                  self.items[item] -= 1
                  print(f"{self.name} has used {item}")
            else:
                  print(f"{self.name} doesnt have this item available")

if __name__ == "__main__":
      trainer = Trainer("Manao foda")
      pokemon = Pokemon("Thales peida molhado", "Eng comp", 10, 2, 30, ["Cagada explosiva", "Peido sonico", "Estudo com faca"])
      
      trainer.catch_pokemon(pokemon)
      trainer.show_roster()
      trainer.use_item("Potion")
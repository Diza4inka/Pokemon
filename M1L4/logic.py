from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.num = self.get_num()
        self.hp = randint(1,100)
        self.power = randint(10,20)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_shiny'])
        else:
            return "https://yandex.ru/images/search?pos=4&from=tabbar&img_url=https%3A%2F%2Fimg.freepik.com%2Fpremium-photo%2Fgirl-pikachu_551707-69798.jpg%3Fsemt%3Dais_hybrid%26w%3D740&text=gbrtrfxe&rpt=simage&lr=53"
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def get_num(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['id'])
        else:
            return "Pikachu"
        
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}, Номер твоего покемона: {self.num}, сила - {self.power}, здоровье - {self.hp}"
        

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def info(self):
        return f"Номер твоего покемона: {self.num}"
    
class Wizard(Pokemon):
    pass

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "
    




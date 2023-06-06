class Card: 
    def __init__(self, name, number, arcana, suit, img, fortune_telling, keywords, meanings):
        self.name = name
        self.number = number
        self.arcana = arcana
        self.suit = suit
        self.img = img
        self.fortune_telling = []
        self.keywords = []
        self.meanings = {
            'light': [],
            'shadow': []
        }
        # self.archetype = archetype
        # self.hebrew = hebrew
        # self.element = element
        
        

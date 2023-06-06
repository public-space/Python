import json
from card import Card

# ? In the load_cards_from_json function, we use json.load to load the JSON data from the file.

def load_cards_from_json(file_path): 
    with open(file_path) as file: 
        json_data = json.load(file)
        
    cards_data = json_data['cards'] 
    #* data['cards'] is referencing the JSON's key 'cards' which is a list of dictionaries
    
    cards = []
    
# ? We then use a for loop to iterate over the list of dictionaries in the JSON data. 
# ! For each dictionary, we create a new Card object and append it to the cards list.
 
    for card_data in cards_data: 
        card = Card(
            name = card_data['name'],
            number = card_data['number'],
            arcana = card_data['arcana'],
            suit = card_data['suit'],
            img = card_data['img'],
            fortune_telling = card_data['fortune_telling'],
            keywords = card_data['keywords'],
            meanings = card_data['meanings']
            # archetype = card_data['Archetype'],
            # hebrew = card_data['Hebrew Alphabet'],
            # element = card_data['Elemental']            
        )
        
        cards.append(card)
        
file_path = "C:/Users/publi/Python/Tarot/rider-waite/tarot-images.json"
cards = load_cards_from_json(file_path)

# for card in cards: 
#     print(card.name)

print(cards[0].name)
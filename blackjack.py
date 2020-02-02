from flask import Flask, jsonify, abort
from random import choice


app = Flask(__name__)

class Game():

    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    values = {
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "10" : 10,
        "J" : 10,
        "Q" : 10,
        "K" : 10,
        "A" : 11
    }

    value_of_A_over_21 = {
        "A" : 1
    }

    hand = []
    def add_card(self): 
        card = choice(self.cards)
        self.hand.append(card)
        return card

    def count_total(self):
        total = 0
        for card in self.hand:
            total += self.values[card]
        if total > 21:
            total = 0
            for card in self.hand:
                if card != "A":
                    total += self.values[card]
                else:
                    total += self.value_of_A_over_21[card]
        return total

game = Game()


@app.route('/blackjack/api/hand', methods=['GET'])
def get_hand():
    return jsonify({'hand': game.hand})

@app.route('/blackjack/api/hand/total', methods=['GET'])
def get_total():   
    return jsonify({'cards_value': game.count_total()})

@app.route('/blackjack/api/start', methods=['POST'])
def start():
    if len(game.hand) > 0:
        abort(400, 'Can be called only at the start of the game')
    for add in range(2):
        game.add_card()
    return jsonify({'in_hand': game.hand, 'cards_value': game.count_total()}), 201

@app.route('/blackjack/api/hand/one', methods=['PUT'])
def get_one():
    if len(game.hand) < 2:
        abort(400, 'First call /blackjack/api/start to start a game')
    card = game.add_card()
    return jsonify({'new_card': card, 'in_hand': game.hand, 'cards_value': game.count_total()})
    

if __name__ == '__main__':
    app.run(debug=True)
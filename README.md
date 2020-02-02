# ČSOB interview tasks


## Math parser

GET Request /api/math/1plus2plus3minus4minus8plus57:

    curl --location --request GET 'http://127.0.0.1:5000/api/math/1plus2plus3minus4minus8plus57'
Response 200 OK:
 `{"result": "51"}`

Accepts a string of numbers and plus or minus operators, evaluates it and returns a result as a JSON response.

## Blackjack Scorer

POST Request /blackjack/api/start:

    curl --location --request POST 'http://127.0.0.1:5000/blackjack/api/start' \ --header 'Content-Type: application/json'
    
Response 201 CREATED:

    {"cards_value": 7, "in_hand": ["4", "3"]}
    
Starts a new game, client gets two randomly selected cards.

  
PUT Request /blackjack/api/hand/one:

    curl --location --request PUT 'http://127.0.0.1:5000/blackjack/api/hand/one' \ --header 'Content-Type: application/json'

Response 200 OK:

    {"cards_value": 17, "in_hand": ["4", "3", "J"], "new_card": "J"}
    
Client wants another card.


GET Request /blackjack/api/hand:

    curl --location --request GET 'http://127.0.0.1:5000/blackjack/api/hand' \ --header 'Content-Type: application/json'
Response 200 OK:

     {"hand": []}
     
 Gets current state of cards in client's hand.
 

GET Request /blackjack/api/hand/total:

    curl --location --request GET 'http://127.0.0.1:5000/blackjack/api/hand/total' \ --header 'Content-Type: application/json'
Response 200 OK:

    {"cards_value": 17}
    
Gets total value of cards in client's hand. Scoring is based on Blackjack rules.

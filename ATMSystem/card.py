class Card:
    def __init__(self, card_number, pin):
        self._card_number = card_number
        self._pin = pin
        
    def get_card_number(self):
        return self._card_number

    def get_pin(self):
        return self._pin
    
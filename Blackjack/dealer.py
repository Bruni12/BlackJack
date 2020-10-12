

class DealerAI():
    def __init__(self,dealer_score):
        self._dealer_score = dealer_score # What the dealers score is.

    @property
    def dealer_score(self):
        return self._dealer_score

    @dealer_score.setter
    def dealer_score(self,value):
        self._dealer_score = value

    ########
    #The dealer must hit if his total is below 17
    ########
    def is_hit(self):
        if int(self._dealer_score) > 17:
            return False
        else:
            return True

    #####
    #If the dealer has any high aces (counted as 11) as part of his total, 
    #he must hit while his count is below 18.        
    #####
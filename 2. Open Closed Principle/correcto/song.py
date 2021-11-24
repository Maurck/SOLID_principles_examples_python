from mesurable import Mesurable

class Song(Mesurable):
    total_length = 5
    sent_length = 1

    def get_sent_length(self):
        return self.sent_length
    
    def get_total_length(self):
        return self.total_length
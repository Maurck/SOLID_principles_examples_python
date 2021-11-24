from mesurable import Mesurable

class File(Mesurable):
    total_length = 10
    sent_length = 1

    def get_sent_length(self):
        return self.sent_length
    
    def get_total_length(self):
        return self.total_length
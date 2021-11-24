class File:
    total_length = 1
    sent_length = 1
    def __init__(self):
        pass

    def get_length_percentage(self):
        return self.sent_length * 100 / self.total_length

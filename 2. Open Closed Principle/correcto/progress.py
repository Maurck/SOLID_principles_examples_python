from mesurable import Mesurable
from song import Song
from file import File

class Progress:
    def get_sent_length_percentage(self, mesurable: Mesurable):
        return mesurable.get_sent_length_percentage()

if __name__ == '__main__':
    file = File()
    song = Song()
    progress = Progress()

    print(f'El progreso de la cancion es del {progress.get_sent_length_percentage(song)} %')
    print(f'El progreso del archivo es del {progress.get_sent_length_percentage(file)} %')
    print(issubclass(Song, Mesurable))
import pickle
import pkgutil


class Exim:
    file_1 = pkgutil.get_data(__name__,"files/all_birds_list")
    #file_1 = open("all_birds_list", 'rb')
    all_birds_list = pickle.load(file_1)
    all_birds_list_padded = []
    for bird in all_birds_list:
        all_birds_list_padded.append(" " + bird + " ")

    file_2 = pkgutil.get_data(__name__,"files/birdnames_words")
    #file_2 = open("birdnames_words", 'rb')
    birdnames_words = pickle.load(file_2)

    def __init__(self):
        pass

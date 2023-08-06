import pickle
import pkgutil


class Exim:
    file_1 = pkgutil.get_data(__name__,"files/all_birds_list")
    all_birds_list = pickle.loads(file_1)
    all_birds_list_padded = []
    for bird in all_birds_list:
        all_birds_list_padded.append(" " + bird + " ")

    file_2 = pkgutil.get_data(__name__,"files/birdnames_words")
    birdnames_words = pickle.loads(file_2)

    def __init__(self):
        pass

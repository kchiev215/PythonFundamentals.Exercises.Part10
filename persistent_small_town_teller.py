import pickle

from small_town_teller1 import Person, Account, Bank


class PersistenceUtils:
    def write_pickle(self, convert_to_pickle):
        with open('/Users/Thina/Desktop/Python/PythonFundamentals.Exercises.Part10/persistence.pickle', 'w') as f:
            pickle.dump(convert_to_pickle, f)

    def load_pickle(self, file_name):
        with open(file_name, 'r') as f:
            pickle.load(f)

from manager import Manager
from utils.cleaner import Cleaner
from config import PATH_WEAPONS


def get_weapons(path):
    with open(path, 'r') as f:
        str_weapons = f.read()

    cleaner = Cleaner(str_weapons)
    clean_str_weapons = cleaner.clean()
    weapons = clean_str_weapons.split(' ')
    return weapons



if __name__ == "__main__":
    weapons = get_weapons(PATH_WEAPONS)
    manager = Manager(weapons)
    manager.manage_message()

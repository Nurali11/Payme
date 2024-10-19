
class User:
    def check_password(password):
        with open('tekshiruv.txt') as f:
                    for i in f.read().split('\n'):
                        if len(i) > 0:
                            i = i.split(',')
                            if i[3] == password:
                                return i
        return None

class Card:
    def abc():
        pass

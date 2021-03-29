from homework.python_practice1.hero import Hero


class Timo(Hero):
    hp = 2000
    power = 210
    name = "timo"

    def speak_lines(self):
        '''
        重写hero的speak方法，用于police说自己独特的话
        '''
        print("提莫队长正在待命")

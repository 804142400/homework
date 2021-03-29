from homework.python_practice1.hero import Hero


class Police(Hero):
    hp = 3000
    power = 110
    name = "police"

    def speak_lines(self):
        '''
        重写hero的speak方法，用于police说自己独特的话
        '''
        print("见识一下法律的子弹")

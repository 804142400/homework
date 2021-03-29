class Hero:
    """
    每个英雄都有 hp 属性和 power属性，hp 代表血量，power 代表攻击力
    """
    hp = 0
    power = 0
    name = ""

    def fight(self, enemy):
        """
        两方进行一回合制的对打
        :param enemy:
        :param enemy_hp: 敌人的血量
        :param enemy_power:  敌人的攻击力
        :return:
        """
        # 我的血量
        # 通过实例变量的方式调用类变量
        final_hp = self.hp - enemy.power
        enemy_final_hp = enemy.hp - self.power
        if final_hp > enemy_final_hp:
            print(f"我（{self.name}）赢了")
        elif final_hp < enemy_final_hp:
            print(f"我（{self.name}）居然输了")
        else:
            print(f"这次我({self.name})和{enemy.name}打了个平手,下次再战")

    def speak_lines(self):
        """
        调用speak_lines方法，不同的角色会打印（讲出）不同的台词
        timo : 提莫队长正在待命
        police: 见识一下法律的子弹
        :return:
        """

        print("英雄的口头禅")

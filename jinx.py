from hero import Hero


class JINX(Hero):
    hp = 2000
    power = 2000
    name = "jinx"

    # def fight(self, enemy_hp, enemy_power):
    #
    #     final_hp = self.hp - enemy_power
    #     enemy_final_hp = enemy_hp - self.power
    #     if final_hp > enemy_final_hp:
    #         print("ez赢了")
    #     elif final_hp < enemy_final_hp:
    #         print("敌人赢了")
    #     else:
    #         print("我们打平了")


# ez = EZ()
jinx = JINX()
# ez.fight(jinx.hp, jinx.power)

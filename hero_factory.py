from ez import EZ
from jinx import JINX
from police import Police
from timo import Timo


class HeroFactory:
    @staticmethod
    def crate_hero(name):
        if name == "JINX":
            return JINX()
        elif name == "EZ":
            return EZ()
        elif name == "Timo":
            return Timo()
        elif name == "Police":
            return Police()
        else:
            raise Exception("英雄名称不存在")


hero_factory = HeroFactory()
jinx = hero_factory.crate_hero("JINX")
ez = hero_factory.crate_hero("EZ")
timo = hero_factory.crate_hero("Timo")
police = hero_factory.crate_hero("Police")
jinx.speak_lines(ez.name)
ez.speak_lines(jinx.name)
police.speak_lines(timo.name)
timo.speak_lines(police.name)
timo.fight(police.hp, police.power)
police.fight(timo.hp, timo.power)
ez.fight(jinx.hp, jinx.power)
jinx.fight(ez.hp, ez.power)

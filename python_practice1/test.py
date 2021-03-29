from homework.python_practice1.hero_factory import HeroFactory

hero_factory = HeroFactory()
timo = hero_factory.create_hero("timo")
police = hero_factory.create_hero("police")
timo.fight(police)
police.fight(timo)
timo.speak_lines()
police.speak_lines()

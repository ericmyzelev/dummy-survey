from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField(min=0)


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'age']

class Results(Page):
    pass


page_sequence = [MyPage, Results]

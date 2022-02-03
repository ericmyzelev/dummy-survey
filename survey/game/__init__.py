from otree.api import *


doc = """
The is a test survey.
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
    name = models.StringField(label="What is your name?")
    employed = models.BooleanField(
        label="Are you currently employed?",
        choices=[
            [False, 'No'],
            [True, 'Yes'],
        ]
    )
    time_at_current_job = models.IntegerField(min=0, label="How long have you been at your current job (in years)?")


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['name', 'employed']

class Page2(Page):
    form_model = 'player'
    form_fields = ['time_at_current_job']

    @staticmethod
    def is_displayed(player):
        return player.employed

class Results(Page):
    pass

page_sequence = [MyPage, Page2, Results]

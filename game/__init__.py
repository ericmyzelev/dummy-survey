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
    q1 = models.StringField(
        label="1. In general, how would your best friend describe you as a risk taker?",
        choices=[
            [1, 'Avoid risk at all costs'],
            [2, 'Cautious'],
            [3, 'Willing to take risks after completing adequate research'],
            [4, 'A real gambler']
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    q2 = models.StringField(
        label="2. You are on TV game show and can choose one of the following, which would you take?",
        choices=[
            [1, '$1,000 in cash'],
            [2, 'A 50% chance at winning $5,000'],
            [3, 'A 25% chance at winning $10,000'],
            [4, 'A 5% chance at winning $100,000'],
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    q3 = models.StringField(
        label='3. You have just finished saving for a "once-in-a-lifetime" vacation. Three weeks before you plan and leave, you lose your job. You would:',
        choices=[
            [1, 'Cancel the vacation'],
            [2, 'Take a much more modest vacation'],
            [3, 'Go as scheduled, because you need the time to prepare for a job search.'],
            [4, 'Extend your vacation, because this might be your last chance to go first-class'],
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    q4 = models.StringField(
        label="4. If you unexpectedly received $20,000 to invest, what would you do?",
        choices=[
            [1, 'Deposit it into a bank account, money market account or an insured CD'],
            [2, 'Invest it in safe high-quality bonds or bond mutual funds'],
            [3, 'Invest it in stocks or stock mutual funds']
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    q5 = models.StringField(
        label="5. In terms of experience, how comfortable are you investing in stocks or stock mutual funds?",
        choices=[
            [1, 'Not at all comfortable'],
            [2, 'Somewhat comfortable'],
            [3, 'Very Comfortable']
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    q6 = models.StringField(
        label='6. When you think of the word "risk" which of the following words comes to mind first?',
        choices=[
            [1, 'Loss'],
            [2, 'Uncertainty'],
            [3, 'Opportunity'],
            [4, 'Thrill'],
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    q7 = models.StringField(
        label="7. Some experts are predicting the prices of hard assets such as gold, jewels, collectibles and real" +
              " estate to increase in value; bond prices may fall, however, experts tend to agree that government " +
              "bonds are relatively safe. Most of your investment assets are now in high-interest government bonds. " +
              "What would you do?",
        choices = [
            [1, 'Hold the bonds'],
            [2, 'Sell the bonds, put half the proceeds into money market accounts and the other half into hard assets'],
            [3, 'Sell the bonds and put the total proceeds into hard assets'],
            [4, 'Sell the bonds, put total proceeds into hard assets and borrow additional money to buy more'],
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    q8 = models.StringField(
        label="8. Given the best- and worst-case returns of the four investment choices below, which would you prefer?",
        choices=[
            [1, '$200 gain best case; $0 gain or loss worst case'],
            [2, '$800 gain best case; $200 loss worst case'],
            [3, '$2,600 gain best case; $800 loss worst case'],
            [4, '$4,800 gain best case; $2,400 loss worst case'],
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    q9 = models.StringField(
        label="9. Suppose a relative left you an inheritance of $100,000, stipulating in the will that you invest" +
              " ALL of the money in ONE of the following choices. Which one would you select?",
        choices = [
            [1, 'A savings account or money market mutual fund'],
            [2, 'A mutual fund that owns stocks and bonds'],
            [3, 'A portfolio of 15 common stocks'],
            [4, 'Commodities like gold, silver and oil'],
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    q10 = models.StringField(
        label="10. If you had to invest $20,000, which of the following investment choices would you find most appealing?",
        choices=[
            [1, '60% in low-risk investments, 30% in medium-risk investments, 10% in high-risk investments'],
            [2, '30% in low-risk investments, 40% in medium-risk investments, 30% in high-risk investments'],
            [3, '10% in low-risk investments, 40% in medium-risk investments, 50% in high-risk investments']
        ],
        widget=widgets.RadioSelect,
        blank=True
    )
    q11 = models.StringField(
        label="11. Your trusted friend and neighbor, an experienced geologist, is putting together a group " +
              "of investors to fund an exploratory gold mining venture. The venture could pay back 50 to 100 " +
              "times the investment if successful. If the mine is a bust, the entire investment is worthless." +
              " Your friend estimates the chance of success is only 20%. If you had the money, "
              "how many months worth of salary would you invest?",
        widget=widgets.RadioSelectHorizontal(),
        choices=[[i, '{}'.format(i)] for i in range(0, 7)],
        blank=True
    )
    income_percentage = models.IntegerField(
        label="12. What percentage of your annual income do you have invested (answers can be over 100)?",
        min=0
    )
    percent_invested_high = models.IntegerField(min=0, label="What percent of your portfolio is invested in high-risk investments?")
    percent_invested_medium = models.IntegerField(min=0, label="What percent of your portfolio is invested in medium-risk investments?")
    percent_invested_low = models.IntegerField(min=0, label="What percent of your portfolio is invested in low-risk investments?")
    investments_10k = models.BooleanField(
        label="Do you currently have at least $10,000 invested or saved?",
        choices = [
            [False, 'No'],
            [True, 'Yes'],
        ]
    )


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['q{}'.format(x) for x in range(1, 12)] + ['income_percentage']

class Page2(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.income_percentage > 0:
            return ['percent_invested_high', 'percent_invested_medium', 'percent_invested_low', 'investments_10k']
        else:
            return ['investments_10k']

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if player.income_percentage > 0 and values['percent_invested_high'] + values['percent_invested_medium'] + values['percent_invested_low'] != 100:
            return 'Your investments must add up to 100%.'

class Results(Page):
    @staticmethod
    def js_vars(player):
        return dict(
            income_percentage = player.income_percentage,
        )

page_sequence = [MyPage, Page2, Results]

from axelrod import Actions, Player, random_choice

C, D = Actions.C, Actions.D

class BetterAndBetter(Player):
    """
    Defects with probability of '(1000 - current turn) / 1000'.
    Therefore it is less and less likely to defect as the round goes on.

    Names:
        - Better and Better: [PRISON1998]_

    """

    name = 'Better and Better'
    classifier = {
        'memory_depth': float('inf'),
        'stochastic': True,
        'makes_use_of': set(),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def strategy(self, opponent):
        current_round = len(self.history) + 1
        probability = current_round / 1000
        return random_choice(probability)


class KnowledgeableBetterAndBetter(Player):
    """
    This strategy is based on 'Better And Better' but will defect with
    probability of 'current turn / total no. of turns'.

    Names:
        - Knowledgeable Better and Better: Original name by Adam Pohl
    """

    name = 'Knowledgeable Better and Better'
    classifier = {
        'memory_depth': float('inf'),
        'stochastic': True,
        'makes_use_of': set(['length']),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def strategy(self, opponent):
        current_round = len(self.history) + 1
        expected_length = self.match_attributes['length']
        probability = current_round / expected_length
        return random_choice(probability)

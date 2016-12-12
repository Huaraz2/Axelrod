"""Test for the Better and Better strategy."""

import axelrod

from .test_player import TestPlayer

C, D = axelrod.Actions.C, axelrod.Actions.D

class TestBetterAndBetter(TestPlayer):

    name = "Better and Better"
    player = axelrod.BetterAndBetter
    expected_classifier = {
        'memory_depth': float('inf'),
        'stochastic': True,
        'makes_use_of': set(),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def test_strategy(self):
        """
        Test that the strategy gives expected behaviour
        """

        self.responses_test([], [], [D, D, D, D, C, D, D, D, D, D], random_seed=6)
        self.responses_test([], [], [D, D, D, D, D, D, D, D, D, D], random_seed=8)

class TestKnowledgeableBetterAndBetter(TestPlayer):

    name = "Knowledgeable Better and Better"
    player = axelrod.KnowledgeableBetterAndBetter
    expected_classifier = {
        'memory_depth': float('inf'),
        'stochastic': True,
        'makes_use_of': set(['length']),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def test_strategy(self):
        """
        Test that the strategy gives expected behaviour
        """
        axelrod.seed(1)
        opponent = axelrod.Cooperator()
        player = axelrod.KnowledgeableBetterAndBetter()
        match = axelrod.Match((opponent, player), turns=5)
        self.assertEqual(match.play(), [('C', 'C'),
                                        ('C', 'D'),
                                        ('C', 'D'),
                                        ('C', 'C'),
                                        ('C', 'C')])

        # Test that behaviour does not depend on opponent
        opponent = axelrod.Defector()
        player = axelrod.KnowledgeableBetterAndBetter()
        axelrod.seed(1)
        match = axelrod.Match((opponent, player), turns=5)
        self.assertEqual(match.play(), [('D', 'C'),
                                        ('D', 'D'),
                                        ('D', 'D'),
                                        ('D', 'C'),
                                        ('D', 'C')])

        # Test that behaviour changes when does not know length.
        axelrod.seed(1)
        match = axelrod.Match((opponent, player), turns=5,
                              match_attributes={'length': float('inf')})
        self.assertEqual(match.play(), [('D', 'D'),
                                        ('D', 'D'),
                                        ('D', 'D'),
                                        ('D', 'D'),
                                        ('D', 'D')])

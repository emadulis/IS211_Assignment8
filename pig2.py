#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week8 game module"""

import random
import sys
import time


class Die:
    """ A Die class."""

    def __init__(self):
        self.value = 0
        seed = 0

    def roll(self):
        self.value = random.randint(1, 7)


class Player:
    """ A Players class."""

    def __init__(self):
        self.turn = False
        self.roll = True
        self.hold = False
        self.score = 0
        self.name = None

    def decide(self):
        """This function will prompt to play."""
        decision = str(
            raw_input('Do you want to Roll (r) or Hold (h)? ')).lower()
        if decision == 'h':
            self.hold = True
            self.roll = False
        elif decision == 'r':
            self.hold = False
            self.roll = True
        else:
            print('Invalid key!!!. Please enter Roll (r) or Hold (h) ".')
            self.decide()


class Computer(Player):
    """A computer player class."""

    def __init__(self):
        Player.__init__(self)
        self.name = "Computer"
        self.turn = False
        self.roll = True
        self.hold = False
        self.score = 0

    def decide(self):
        """This function will score the game."""
        min_hold = 25
        max_hold = 100 - self.score
        if self.score < min_hold:
            return "roll"
        elif self.score >= max_hold:
            return "hold"



class Human(Player):
    """ A human player class."""

    def __init__(self):
        self.name = None
        Player.__init__(self)


class Game:
    """ A Game class."""

    def __init__(self, player1, player2, die):
        """ A init function that will allow to play the game."""
        self.turn_score = 0
        self.die = Die()
        self.player1 = player1
        self.player2 = player2
        self.player1.score = 0
        self.player2.score = 0
        self.player1.name = "Player 1"
        self.player2.name = "Player 2"

        print raw_input("Please press Enter to roll the coin and begin the game.")
        tossed = random.randint(1, 2)
        if tossed == 1:
            self.current_player = self.player1
            print "Player 1 got the toss and will go first."
        elif tossed == 2:
            self.current_player = self.player2
            print "Player 2got the toss and will go first."
        self.turn()

    def next_turn(self):
        """ A function that will rotate the chance to pick an option."""
        self.turn_score = 0
        if self.player1.score >= 100:
            print "Player 1 wins!"
            print "Score:", self.player1.score
            self.endgame()
            newGame()
        elif self.player2.score >= 100:
            print "Player 2 wins!"
            print "Score:", self.player2.score
            self.endgame()
            newGame()
        else:
            if self.current_player == self.player1:
                self.current_player = self.player2
            elif self.current_player == self.player2:
                self.current_player = self.player1
            print "Next turn, it is ", self.current_player.name, "'s turn."
            self.turn()

    def turn(self):
        """ Turn function."""
        self.die.roll()
        if (self.die.value == 1):
            print "No points added, your turn is over."
            print "Player 1 Score:", self.player1.score
            print "Player 2 Score:", self.player2.score
            self.turn_score = 0
            self.next_turn()
        else:
            self.turn_score = self.turn_score + self.die.value
            print "You just roll a:", self.die.value
            print "Your current value is:", self.turn_score
            print "Player 1 Score:", self.player1.score
            print "Player 2 Score:", self.player2.score
            self.current_player.decide()
            if (self.current_player.hold == True and self.current_player.roll == False):
                self.current_player.score = self.current_player.score + self.turn_score
                self.next_turn()
            elif (self.current_player.hold == False and self.current_player.roll == True):
                self.turn()

    def endgame(self):
        """ A endgame function."""
        self.player1 = None
        self.player2 = None
        self.die = None
        self.turn_score = None


class Proxy(Game):
    """ A proxy class."""

    def __init__(self):
        self.timed = float(time.time() + 60)

    def timeCheck(self, timed):
        if (self.timed < float(time.time())):
            print "Your time is up!"


def newGame():
    """ A new hgame function."""
    new = raw_input(
        'To start the game enter start (s) or timed (t) ')
    if new.lower() == "s":
        player1 = raw_input("Player 1: Human (h) or Computer (c)? ").lower()
        player2 = raw_input("Player 2: Human (h) or Computer (c)? ").lower()
        die = Die()
        if player1 == "h":
            player1 = Human()
        elif player1 == "c":
            player1 = Computer()
        if player2 == "h":
            player2 = Human()
        elif player2 == "c":
            player2 = Computer()
        Game(player1, player2, die)
    if new.lower() == "t":
        timed = float(time.time() + 60)
    else:
        print 'Please enter the correct key start(s) or timed (t) to begin.'
        newGame()


if __name__ == '__main__':
    newGame()

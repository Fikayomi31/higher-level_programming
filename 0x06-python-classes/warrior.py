#!/usr/bin/python3
import random
import math

"""
Sample output
Sam attacks paul and deal 9 damag
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attavks Paul and deal 19 damage
Paul is down to -9 health
Paul is died and Sam is Victoriou
Game over
"""
"""Defining a warriors class"""
class Warrior:

    def __init__(self, name="", health=0, attMax=0, blockMax=0):
        """Initializing the class warrior
        name: name of the warrior
        health: health of the warrior
        attMax: attack by the warrior
        blockMax: block by the warrior
        """
        self.name = name
        self.health = health
        self.attMax = attMax
        self.blockMax = blockMax

    # method to attacks
    def attack(self):
        attAmt = self.attMax * (random.random() + .5)

        return attAmt

    # method to block
    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt


""" Defining battle class"""
class Battle:
    
    def startFight(self, warrior1, warrior2):
    
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warriorA_Att = warriorA.attack()

        warriorB_block = warriorB.block()

        damage_warriorB = math.ceil(warriorA_Att - warriorB_block)

        warriorB.health -= damage_warriorB

        print("{} attack {} and deals {} damage".format(warriorA.name, warriorB.name, damage_warriorB))

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

maximus = Warrior("Maximus", 50, 20, 10)
galaxon = Warrior("Galaxon", 50, 20, 10)

battle = Battle()

battle.startFight(maximus, galaxon)


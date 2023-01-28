from game_data import data
from art import logo, vs
from random import randint
import os
score = 0
incorrect = False

def choosePersons():
  """Chooses two random people from the data list and returns them"""
  randomPerson1 = data[randint(0,len(data) -1)]
  randomPerson2 = data[randint(0,len(data) -1)]

  if randomPerson2["name"] == randomPerson1["name"]:
    randomPerson2 = data[randint(0,len(data) -1)]
  return [randomPerson1, randomPerson2]
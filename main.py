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


def who_is_famous(item1,item2):
  """Takes in two inputs and compares which input has a higher follower_count and returns it"""
  famous = ""
  if item1['follower_count'] > item2['follower_count']:
    famous = item1["name"]
  else:
    famous = item2["name"]
  return famous

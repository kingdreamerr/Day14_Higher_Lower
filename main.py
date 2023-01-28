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


people = choosePersons()
person2 = people[1]

print(logo)
while not incorrect:
  person1 = person2
  people = choosePersons()
  person2 = people[0]

  print(f'Compare A: {person1["name"]} is a {person1["description"]} from {person1["country"]}')
  print(vs)
  print(f'Against B: {person2["name"]} is a {person2["description"]} from {person2["country"]}')

  guess = input("Who has more followers? 'A' or 'B' : ").lower()
  isGuessCorrect = False
  while not isGuessCorrect:
    if guess == "a" or guess == "b":
        isGuessCorrect = True
    else:
      guess = input("incorrect input \n please choose between A and B : ")
  
  correctPerson = who_is_famous(person1,person2)

  if(guess == "a"):
    selectedPerson = {}
    selectedPerson = person1
  else:
    selectedPerson = person2

  os.system("clear")
  print(logo)

  if selectedPerson["name"] == correctPerson:
    score += 1
    print(f"you're right! current score {score}.")
  else:
    print(f'Incorrect game over your score is {score}')
    incorrect = True

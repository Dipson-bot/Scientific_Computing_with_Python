import copy
import random

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for _ in range(value):
        self.contents.append(key)

  def draw(self, number):
    if number >= len(self.contents):
      drawn_balls = self.contents[:]
      self.contents.clear()
      return drawn_balls
    balls = []
    for _ in range(number):
      choice = random.randrange(len(self.contents))
      balls.append(self.contents.pop(choice))
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected_no_of_balls = [expected_balls[key] for key in expected_balls]
  successes = 0

  for _ in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    balls = new_hat.draw(num_balls_drawn)

    no_of_balls = [balls.count(key) for key in expected_balls]

    if all(no_of_balls[i] >= expected_no_of_balls[i] for i in range(len(expected_no_of_balls))):
      successes += 1

  return successes / num_experiments

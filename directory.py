import os

def test():

  path = os.path.dirname(__file__)
  print(path)

  path2 = os.path.dirname(path)
  print(path2)

test()
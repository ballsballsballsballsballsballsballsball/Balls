from random import choice as superballs

  
class Ball:
  balls = "balls"
  isball = True
  extremeball = ("Ball", 69)


balls = Ball()

def evenbetterballs():
  while True:
    print("".join(superballs((str.upper, str.lower ))(c) for c in balls.balls))

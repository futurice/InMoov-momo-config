def shrug():
  i01.startedGesture()

  fullspeed()

  i01.moveArm("right", 30, 38, 90, 135)
  i01.moveArm("left", 18, 20, 90, 125)

  sleep(1)

  i01.moveArm("right", 20, 98, 90, 94)
  i01.moveArm("left", 8, 90, 90, 97)

  sleep(1)

  i01.finishedGesture()

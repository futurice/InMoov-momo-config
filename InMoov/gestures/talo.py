def talo():

  i01.startedGesture()

  fullspeed()

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.moveArm("left", 150, 90, 135, 0)
  i01.moveArm("right", 180, 85, 148, 0)

  sleep(5)

  i01.moveArm("left", 150, 115, 135, 0)
  i01.moveArm("right", 180, 100, 148, 0)

  sleep(3)

  i01.moveArm("left", 150, 115, 80, 0)
  i01.moveArm("right", 180, 100, 75, 0)

  sleep(3)

  # rest

  i01.moveArm("left", 0, 90, 0, 0)
  i01.moveArm("right", 0, 90, 0, 0)

  sleep(2)

  i01.finishedGesture()

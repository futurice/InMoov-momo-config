def vasara():
  i01.startedGesture()

  fullspeed()

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')

  # hammer up
  i01.moveArm("right", 140, 110, 120, 0)

  sleep(3)

  # hammer down
  i01.moveArm("right", 40, 110, 120, 0)

  sleep(1)

  i01.moveArm("right", 140, 110, 120, 0)

  sleep(1)

  i01.moveArm("right", 40, 110, 120, 0)

  sleep(1)

  #rest
  i01.moveArm("right", 0, 90, 0, 0)

  sleep(2)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')

  i01.finishedGesture()


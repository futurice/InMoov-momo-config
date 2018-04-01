def auto():
  i01.startedGesture()

  fullspeed()

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')

  sleep(2)

  i01.moveArm("left", 180, 60, 120, 25)
  i01.moveArm("right", 180, 130, 50, 25)

  sleep(2)

  i01.moveArm("left", 180, 130, 50, 25)
  i01.moveArm("right", 180, 60, 120, 25)

  sleep(2)

  i01.moveArm("left", 180, 60, 120, 25)
  i01.moveArm("right", 180, 130, 50, 25)

  sleep(2)

  i01.moveArm("left", 180, 130, 50, 25)
  i01.moveArm("right", 180, 60, 120, 25)

  sleep(1)

  i01.moveArm("left", 0, 90, 0, 0)
  i01.moveArm("right", 0, 90, 0, 0) 

  sleep(3)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.finishedGesture()

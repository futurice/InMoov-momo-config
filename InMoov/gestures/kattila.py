def kattila():

  i01.startedGesture()

  fullspeed()

  # make fists

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')

  # palms a bit up

  i01.moveHand("right",180,180,180,180,180,155)
  i01.moveHand("left",180,180,180,180,180,62)

  # arms up

  i01.moveArm("left", 95, 90, 100, 0)
  i01.moveArm("right", 180, 85, 100, 0)

  sleep(5)

  # do the shake

  i01.moveArm("left", 65, 90, 100, 0)
  i01.moveArm("right", 130, 85, 100, 0)

  sleep(1)

  i01.moveArm("left", 95, 90, 100, 0)
  i01.moveArm("right", 180, 85, 100, 0)

  sleep(1)

  i01.moveArm("left", 65, 90, 100, 0)
  i01.moveArm("right", 130, 85, 100, 0)

  sleep(1)

  # rest

  i01.moveArm("left", 0, 90, 0, 0)
  i01.moveArm("right", 0, 90, 0, 0)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  sleep(2)

  i01.finishedGesture()

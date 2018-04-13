def juna():
  i01.startedGesture()

  fullspeed()
  i01.setArmVelocity("right", 50, -1, -1, -1)

  # make a fist
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')

  # palm up (only the last digit matters)
  i01.moveHand("right",180,180,180,180,180,160)

  # arm up
  i01.moveArm("right", 100, 85, 115, 90)

  sleep(4)

  # fingers to train sign
  print commands.getoutput('/bin/echo "1000,550,600,1000,1000" | /usr/bin/nc localhost 10000')

  sleep(2)

  # arm forward
  i01.moveArm("right", 40, 80, 165, 0)

  sleep(2)

  # arm back
  i01.moveArm("right", 100, 85, 115, 90)

  sleep(2)

  # arm forward
  i01.moveArm("right", 40, 80, 165, 0)

  sleep(3)

  # rest

  i01.moveArm("left", 8, 90, 90, 90)
  i01.moveArm("right", 20, 90, 90, 97)

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.finishedGesture()

def pallo():

  i01.startedGesture()

  fullspeed()

  # open hands

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  # wrists to rest
  # bring arms together in front of face

  i01.moveHand("right",180,180,180,180,180,158)
  i01.moveHand("left",180,180,180,180,180,58)

  i01.moveArm("right", 100, 78, 153, 100)
  sleep(1)
  i01.moveArm("left", 90, 65, 143, 90)

  sleep(4)

  momotalk("pallo")

  sleep(1)

  # try to trace a ball

  i01.setArmVelocity("right", 30, -1, -1, -1)
  i01.setArmVelocity("left", 30, -1, -1, -1)

  i01.moveHand("right",180,180,180,180,180,166)
  i01.moveHand("left",180,180,180,180,180,54)
  
  i01.moveArm("right", 65, 88, 153, 100)
  i01.moveArm("left", 55, 78, 143, 90)

  sleep(0.7)

  i01.moveHand("right",180,180,180,180,180,168)
  i01.moveHand("left",180,180,180,180,180,50)
  i01.moveArm("right", 55, 97, 153, 100)
  i01.moveArm("left", 45, 87, 143, 90)

  sleep(0.5)

  i01.moveHand("right",180,180,180,180,180,174)
  i01.moveHand("left",180,180,180,180,180,46)
  i01.moveArm("right", 35, 85, 153, 100)
  i01.moveArm("left", 25, 75, 143, 90)

  sleep(0.5)

  i01.moveHand("right",180,180,180,180,180,180)
  i01.moveHand("left",180,180,180,180,180,42)
  i01.moveArm("right", 35, 52, 153, 100)
  i01.moveArm("left", 25, 42, 143, 90)

  sleep(3)

  # rest

  i01.moveArm("left", 8, 90, 90, 90)
  i01.moveArm("right", 20, 90, 90, 97)

  i01.moveHand("right",180,180,180,180,180,167)
  i01.moveHand("left",180,180,180,180,180,50)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  sleep(2)

  i01.finishedGesture()

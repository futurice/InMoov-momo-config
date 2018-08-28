def pallo():

  i01.startedGesture()

  fullspeed()
  rest()

  # open hands

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  # wrists to rest
  # bring arms together in front of face

  i01.moveHand("right",180,180,180,180,180,149)
  i01.moveHand("left",180,180,180,180,180,61)

  i01.moveArm("right", 100, 78, 153, 100)
  i01.moveArm("left", 74, 63, 143, 90)

  sleep(4)

  #momotalk("pallo")

  sleep(1)

  # try to trace a ball

  i01.setArmVelocity("right", 30, -1, -1, -1)
  i01.setArmVelocity("left", 30, -1, -1, -1)

  i01.moveHand("right",180,180,180,180,180,155)
  i01.moveHand("left",180,180,180,180,180,57)

  i01.moveArm("right", 65, 88, 153, 100)
  i01.moveArm("left", 52, 76, 143, 90)

  sleep(0.7)

  i01.moveHand("right",180,180,180,180,180,157)
  i01.moveHand("left",180,180,180,180,180,53)
  i01.moveArm("right", 50, 97, 153, 100)
  i01.moveArm("left", 40, 87, 143, 90)

  sleep(0.5)

  i01.moveHand("right",180,180,180,180,180,163)
  i01.moveHand("left",180,180,180,180,180,46)
  i01.moveArm("right", 35, 85, 153, 100)
  i01.moveArm("left", 25, 75, 143, 90)

  sleep(0.5)

  i01.moveHand("right",180,180,180,180,180,165)
  i01.moveHand("left",180,180,180,180,180,44)
  i01.moveArm("right", 35, 65, 148, 100)
  i01.moveArm("left", 25, 55, 138, 90)

  sleep(0.7)

  i01.moveHand("right",180,180,180,180,180,170)
  i01.moveHand("left",180,180,180,180,180,40)
  i01.moveArm("right", 40, 58, 143, 100)
  i01.moveArm("left", 25, 42, 133, 90)

  sleep(3)

  rest()

  i01.finishedGesture()

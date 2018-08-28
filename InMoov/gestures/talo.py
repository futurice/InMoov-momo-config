def talo():

  i01.startedGesture()

  fullspeed()
  rest()

  # open hands

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')

  # wrists to rest
  # bring arms together in front of face

  i01.moveHand("right",180,180,180,180,180,158)
  i01.moveHand("left",180,180,180,180,180,54)

  i01.moveArm("right", 90, 82, 174, 100)
  sleep(1)
  i01.moveArm("left", 90, 67, 157, 90)

  sleep(6)

  momotalk("talo")

  sleep(1)

  # take them apart a notch

  i01.moveArm("right", 85, 102, 155, 100)
  i01.moveArm("left", 75, 89, 145, 90)

  sleep(2)

  # bring them down

  i01.moveArm("right", 85, 96, 100, 0)
  i01.moveArm("left", 75, 84, 95, 0)

  sleep(4)

  rest()

  i01.finishedGesture()

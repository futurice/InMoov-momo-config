def talo():

  i01.startedGesture()

  fullspeed()

  # open hands

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  # wrists to rest
  # bring arms together in front of face

  i01.moveHand("right",180,180,180,180,180,143)
  i01.moveHand("left",180,180,180,180,180,72)

  i01.moveArm("right", 100, 84, 168, 100)
  sleep(1)
  i01.moveArm("left", 90, 65, 157, 90)

  sleep(6)

  i01.moveHand("right",180,180,180,180,180,149)
  i01.moveHand("left",180,180,180,180,180,68)

  # take them apart a notch


  i01.moveArm("right", 85, 108, 155, 100)
  i01.moveArm("left", 75, 89, 145, 90)

  sleep(2)

  # bring them down

  i01.moveArm("right", 85, 102, 100, 0)
  i01.moveArm("left", 75, 84, 95, 0)

  sleep(4)

  # rest

  i01.moveArm("left", 8, 90, 90, 90)
  i01.moveArm("right", 20, 90, 90, 97)

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  sleep(2)

  i01.finishedGesture()

def talo():

  i01.startedGesture()

  fullspeed()

  # open hands

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  # wrists to rest
  # bring arms together in front of face

  i01.moveHand("right",180,180,180,180,180,143)
  i01.moveHand("left",180,180,180,180,180,70)

  i01.moveArm("right", 100, 84, 168, 100)
  sleep(1)
  i01.moveArm("left", 90, 65, 155, 90)

  sleep(5)

  # take them apart a notch

  i01.moveArm("left", 90, 81, 155, 90)
  i01.moveArm("right", 100, 105, 164, 100)

  sleep(3)

  # bring them down

  i01.moveArm("left", 90, 84, 125, 0)
  i01.moveArm("right", 100, 102, 130, 0)

  sleep(3)

  # rest

  i01.moveArm("left", 8, 90, 90, 90)
  i01.moveArm("right", 20, 90, 90, 97)

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  sleep(2)

  i01.finishedGesture()

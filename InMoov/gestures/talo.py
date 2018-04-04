def talo():

  i01.startedGesture()

  fullspeed()

  # open hands

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  # wrists to rest

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  sleep(1)

  # bring arms together in front of face

  i01.moveArm("left", 150, 90, 135, 0)
  i01.moveArm("right", 180, 85, 148, 0)

  sleep(5)

  # take them apart a notch

  i01.moveArm("left", 150, 115, 135, 0)
  i01.moveArm("right", 180, 100, 148, 0)

  sleep(2)

  # bring them down

  i01.moveArm("left", 150, 115, 80, 0)
  i01.moveArm("right", 180, 100, 75, 0)

  sleep(2)

  # rest

  i01.moveArm("left", 0, 90, 0, 0)
  i01.moveArm("right", 0, 90, 0, 0)

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')  

  sleep(2)

  i01.finishedGesture()

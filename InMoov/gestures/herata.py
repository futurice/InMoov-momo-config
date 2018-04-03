def herata():

  i01.startedGesture()

  fullspeed()

  # palms down

  i01.moveHand("right",180,180,180,180,180,0)
  i01.moveHand("left",180,180,180,180,180,180)

  # fists

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')

  # bring hands in front of the face

  i01.moveArm("left", 150, 90, 140, 0)
  i01.moveArm("right", 180, 90, 180, 0)

  # here we would want to tilt the wrists up a bit to make this work

  sleep(5)

  # waking gesture with fingers

  print commands.getoutput('/bin/echo "50,50,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,900,900,900" | /usr/bin/nc localhost 10001')

  sleep(3)

  # rest

  i01.moveArm("left", 0, 90, 0, 0)
  i01.moveArm("right", 0, 90, 0, 0)

  i01.moveHand("right",180,180,180,180,180,90)
  i01.moveHand("left",180,180,180,180,180,90)
  
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  sleep(2)

  i01.finishedGesture()


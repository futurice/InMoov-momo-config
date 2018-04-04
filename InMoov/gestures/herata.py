def herata():

  i01.startedGesture()

  fullspeed()

  # palms down

  i01.moveHand("right",180,180,180,180,180,135)
  i01.moveHand("left",180,180,180,180,180,80)

  # fists

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')

  # bring hands in front of the face

  i01.moveArm("left", 90, 70, 162, 90)
  i01.moveArm("right", 100, 80, 174, 97)

  # here we would want to tilt the wrists up a bit to make this work

  sleep(6)

  # waking gesture with fingers

  print commands.getoutput('/bin/echo "50,50,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,900,900,900" | /usr/bin/nc localhost 10001')

  sleep(10)
  exit()

  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 10001')

  sleep(1)

  # rest
  
  i01.moveArm("left", 8, 90, 90, 90)
  i01.moveArm("right", 20, 90, 90, 97)

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  sleep(2)

  i01.finishedGesture()

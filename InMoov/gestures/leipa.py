def leipa():
  i01.startedGesture()
  fullspeed()

  # make fists
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')

  # right arm up first, goes higher, palm down
  i01.moveHand("right",180,180,180,180,180,163)
  i01.moveArm("right", 75, 73, 160, 129)
  sleep(1)

  # left arm up and palm up
  i01.moveHand("left",180,180,180,180,180,37)
  i01.moveArm("left", 71, 36, 146, 120)

  sleep(4)

  momotalk("leipa")

  sleep(1)

  i01.moveArm("right", 75, 42, 160, 129)
  i01.moveArm("left", 71, 66, 146, 120)

  sleep(0.5)

  i01.moveArm("right", 75, 108, 160, 129)
  i01.moveArm("left", 71, 26, 146, 120)

  sleep(0.5)

  i01.moveArm("right", 75, 42, 160, 129)
  i01.moveArm("left", 71, 66, 146, 120)

  sleep(0.5)

  i01.moveArm("right", 75, 108, 160, 129)
  i01.moveArm("left", 71, 26, 146, 120)

  sleep(0.5)

  i01.moveArm("right", 75, 62, 160, 129)
  i01.moveArm("left", 71, 46, 146, 120)

  
  # rest, take left hand down first

  i01.moveArm("left", 8, 90, 90, 90)
  sleep(0.5)

  i01.moveArm("right", 20, 90, 90, 97)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')

  i01.moveHand("right",180,180,180,180,180,167)
  i01.moveHand("left",180,180,180,180,180,50)

  sleep(2)

  i01.finishedGesture()

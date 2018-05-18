def kissa():
  i01.startedGesture()
  fullspeed()
  rest()

  # make fists
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "600,50,50,50,50" | /usr/bin/nc localhost 20000')

  # palms down
  i01.moveHand("right",180,180,180,180,180,165)
  i01.moveHand("left",180,180,180,180,180,52)

  sleep(2)

  # right arm up first, goes higher
  i01.moveArm("right", 67, 73, 160, 129)
  sleep(2)

  # left arm up
  i01.moveArm("left", 55, 36, 160, 120)
  sleep(5)

  momotalk("kissa")

  sleep(1)

  print commands.getoutput('/bin/echo "50,400,500,400,400" | /usr/bin/nc localhost 10000')

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,161)
  i01.moveArm("right", 80, 66, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,171)
  i01.moveArm("right", 60, 74, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,161)
  i01.moveArm("right", 80, 66, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,171)
  i01.moveArm("right", 60, 74, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,161)
  i01.moveArm("right", 80, 66, 160, 129)
  sleep(0.8)

  i01.moveHand("right",180,180,180,180,180,164)

  sleep(3)

  # custom rest, take left hand down first

  i01.moveArm("left", 8, 90, 90, 90)
  sleep(0.2)

  rest()

  i01.finishedGesture()

def kissa():
  i01.startedGesture()
  fullspeed()

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
  i01.moveArm("right", 75, 66, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,171)
  i01.moveArm("right", 55, 74, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,161)
  i01.moveArm("right", 75, 66, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,171)
  i01.moveArm("right", 55, 74, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,161)
  i01.moveArm("right", 75, 66, 160, 129)
  sleep(0.8)

  i01.moveHand("right",180,180,180,180,180,164)

  sleep(3)

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


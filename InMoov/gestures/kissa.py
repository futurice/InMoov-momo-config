def kissa():
  i01.startedGesture()
  fullspeed()

  # make fists
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  # palms down
  i01.moveHand("right",180,180,180,180,180,146)
  i01.moveHand("left",180,180,180,180,180,71)

  sleep(2)

  # right arm up first, goes higher
  i01.moveArm("right", 65, 71, 160, 129)
  sleep(2)

  # left arm up
  i01.moveArm("left", 51, 36, 160, 120)
  sleep(6)

  print commands.getoutput('/bin/echo "50,400,500,400,400" | /usr/bin/nc localhost 10000')

  # pet the cat
  i01.moveArm("right", 85, 71, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveArm("right", 65, 71, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveArm("right", 85, 71, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveArm("right", 65, 71, 160, 129)
  sleep(0.8)
  
  # pet the cat
  i01.moveArm("right", 85, 71, 160, 129)
  sleep(0.8)

  sleep(3)

  # rest, take left hand down first

  i01.moveArm("left", 8, 90, 90, 90)
  sleep(1)

  i01.moveArm("right", 20, 90, 90, 97)

  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10001')

  i01.moveHand("right",180,180,180,180,180,147)
  i01.moveHand("left",180,180,180,180,180,70)

  sleep(2)

  i01.finishedGesture()

def kissa():
  i01.startedGesture()
  fullspeed()
  rest()

  # make fists
  print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 10000')
  print commands.getoutput('/bin/echo "600,50,50,50,50" | /usr/bin/nc localhost 20000')

  # palms down
  i01.moveHand("right",180,180,180,180,180,158)
  i01.moveHand("left",180,180,180,180,180,54)

  sleep(2)

  # right arm up first, goes higher
  i01.moveArm("right", 67, 74, 163, 129)

  sleep(0.3)

  # left arm up
  i01.moveArm("left", 50, 33, 160, 120)
  sleep(5)

  momotalk("kissa")

  sleep(1)

  print commands.getoutput('/bin/echo "50,400,500,400,400" | /usr/bin/nc localhost 10000')
  sleep(0.5)
  
  # pet the cat
  i01.moveHand("right",180,180,180,180,180,154)
  i01.moveArm("right", 80, 72, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,162)
  i01.moveArm("right", 60, 80, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,154)
  i01.moveArm("right", 80, 72, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,162)
  i01.moveArm("right", 60, 80, 160, 129)
  sleep(0.8)

  # pet the cat
  i01.moveHand("right",180,180,180,180,180,154)
  i01.moveArm("right", 80, 72, 160, 129)
  sleep(0.8)

  i01.moveHand("right",180,180,180,180,180,157)

  sleep(3)

  rest()
